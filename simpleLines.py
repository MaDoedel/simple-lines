import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import collections  as mc
import pylab as pl
import numpy as np
import random


# We are parsing the input file, knowing that each line follows a specific language specification
# In more complex scenarios, the points/lines could be represented in other formats like JSON, YAML, or XML or follow other languages specifications, requiring maybe some pattern
# Alternatively, one could use lexer/yacc to write a parser for this task, but that would be overkill for this straightforward task.

file = open("input.txt", "r")

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  # This could be useful
  def __eq__(self, point):
    return self.x == point.x and self.y == point.y
  def __hash__(self):
      return hash((self.x, self.y))
  def __repr__(self):
      return f"Point({self.x}, {self.y})"


class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.length = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5 # Euclidean distance

# TODO: Connect 2 lines to a linesegment, thus a single line can't be a single line
# TODO: Print each line linesegment's length descending order
# TODO: Display the lines in different colors

# Some definitions for documentation reasons
lines = []
  
# adjacency list approach
vertices = []
edges = []
adjacencyM = {}

for line in file:
  x1, y1, x2, y2 = line.split(" ")
  point1 = Point(float(x1), float(y1))
  point2 = Point(float(x2), float(y2))
  edges.append(Line(point1, point2))
  lines.append([(float(x1), float(y1)), (float(x2), float(y2))])

  if point1 not in vertices:
    vertices.append(point1)
  if point2 not in vertices:
    vertices.append(point2)

plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Segments')
plt.grid(True)
c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])  
lc = mc.LineCollection(lines, colors=c, linewidths=2)
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
fig.savefig('initial_plot.png')


# Create adjacency matrix
for point in vertices:
    adjacencyM[point] = []

for edge in edges:
  adjacencyM[edge.p1].append(edge.p2)
  adjacencyM[edge.p2].append(edge.p1)

# Identify line segments
lineSegmentCandidates = []
for point, neighboringPoint in adjacencyM.items():
  # Is technically a starter/end
  if len(neighboringPoint) == 1:
    lineSegmentCandidates.append(point)
  # Is a starter/end
  if len(neighboringPoint) > 2:
    lineSegmentCandidates.append(point)

lineSegments = []

#  this took quiet some time
def walkLineSegment(startPoint, adjacencyM, lineSegmentCandidates, visited):
  segments = []
  stack = [(startPoint, [startPoint])]
  
  while stack:
      current, path = stack.pop()
      if current not in visited:
          visited.add(current)
          neighbors = adjacencyM[current]
          for neighbor in neighbors:
              if neighbor in visited:
                  continue
              new_path = path + [neighbor]
              if neighbor in lineSegmentCandidates:
                  segments.append(new_path)
              elif len(adjacencyM[neighbor]) == 2:
                  stack.append((neighbor, new_path))
              else:
                  segments.append(new_path)
  return segments

lineSegments = []
visited = set()
for startPoint in lineSegmentCandidates:
    if startPoint not in visited:
        segments = walkLineSegment(startPoint, adjacencyM, lineSegmentCandidates, visited)
        lineSegments.extend(segments)

#print(lineSegments)

# Rework the result to handle potential inversions or duplications and short linesegments
reworkedLineSegments = []
for segment in lineSegments:
    if len(segment) < 3:
      continue
    reworkedLineSegments.append(segment)

for segment in reworkedLineSegments:
   for index, other_segment in enumerate(reworkedLineSegments):
      if segment == other_segment[::-1]:
         reworkedLineSegments.remove(other_segment)
    
# Prepare the segments for LineCollection
lines = []
for segment in reworkedLineSegments:
    line = [(point.x, point.y) for point in segment]
    lines.append(line)

# Color array for the segments
colors = [(random.random(), random.random(), random.random()) for _ in lines]

# Plotting using LineCollection
lc = mc.LineCollection(lines, colors=colors, linewidths=2)
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
fig.savefig('reworked_plot.png')

segment_lengths = []
for segment in reworkedLineSegments:
  sum = 0
  for i in range(len(segment) - 1):
    sum+= Line(segment[i], segment[i+1]).length
  segment_lengths.append((segment, sum))

sorted_segment_lengths = sorted(segment_lengths, key=lambda x: x[1], reverse=True)
print(sorted_segment_lengths)