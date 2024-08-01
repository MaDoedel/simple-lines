import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib import collections  as mc
import pylab as pl
import numpy as np


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


class Line:
  def __init__(self, p1, p2):
    self.p1 = p1
    self.p2 = p2
    self.length = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5 # Euclidean distance


# Now Arguing farom the nature of this problem, some would use the composite pattern to represent the lines and their conjunctions, calling finally calculate() at this object, which adds all line lengths
# But: How to decide which line is a conjunction of which? Thats the actual algorithmic problem here
# What indead breaks the deal for a simple tree structured implementation, in which each linesegment is a node and lines are leafs, is that we cant have multiple leaf candiates for a node
# Indead, we have to lookup the following leafs for each insert

# for the sace of simplicity I will just make a list of lists...
all_lines = []

# Lets first see what Im dealing with
plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Segments')
plt.grid(True)

lines = []

for line in file:
    # Reason why I prefer python for quick sketches... basically everything works just fine
    x1, y1, x2, y2 = line.split()

    # Technically, the input here currently is a string unless we convert it to a number, which is highly recommended for Euclidean distance
    lines.append([(float(x1), float(y1)), (float(x2), float(y2))])
    all_lines.append([Line(Point(float(x1), float(y1)), Point(float(x2), float(y2)))])

    # Print the coordinates for debugging
    print(f'{x1} {y1} {x2} {y2}')

# Define colors for each line
c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])  # Modify to match the number of lines if necessary

# Create LineCollection
lc = mc.LineCollection(lines, colors=c, linewidths=2)

# Plotting
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
fig.savefig('initial_plot.png')

# We could start considering each line to be a concunction
changed = True
while changed:
  changed = False
  for index, linegement in enumerate(all_lines):
    if not linegement:  # Skip empty lists
      continue

    start = linegement[0].p1
    end = linegement[-1].p2

    candidates_start = []
    candidates_end = []

    for yndex, other_line in enumerate(all_lines):
      # safe one cycle I guess
      if index == yndex:
        continue

      if not other_line:  # Skip empty lists
        continue

      ystart = other_line[0].p1
      yend = other_line[-1].p2

      # can we connect something with the start?
      if (yend == start) or (ystart == start):
        candidates_start.append(yndex)
      if (yend == end) or (ystart == end):
        candidates_end.append(yndex)
    
    # can I connect some lines/linesegments? Of course, if their start and end correspond only to the ones of another line/linesegment
    if len(candidates_start) == 1:
      linesegment = all_lines[candidates_start[0]] + linegement
      all_lines[index] = linesegment
      all_lines[candidates_start[0]] = []
      changed = True

    if len(candidates_end) == 1:
      linesegment = linegement + all_lines[candidates_end[0]]
      all_lines[index] = linesegment
      all_lines[candidates_end[0]] = []
      changed = True
all_lines = [line for line in all_lines if line]

# Print all line segments
for linegement in all_lines:
    for line in linegement:
        print(f"Start: ({line.p1.x}, {line.p1.y}), End: ({line.p2.x}, {line.p2.y})")

# Generate a list of colors
colors = cm.rainbow(np.linspace(0, 1, len(all_lines) ))

# Plot all line segments with different colors
plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Processed Line Segments')
plt.grid(True)

color_index = 0
for linegement in all_lines:
    for line in linegement:
      plt.plot([line.p1.x, line.p2.x], [line.p1.y, line.p2.y], marker='o', color=colors[color_index])
    color_index += 1

plt.savefig('processed_plot.png')
plt.close()