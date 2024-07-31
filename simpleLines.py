import matplotlib.pyplot as plt

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

# for the sace of some simplicity I will just make a list of lists...
all_lines = [[]]

# Lets first see what Im dealing with
plt.figure()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Line Segments')
plt.grid(True)

for line in file:
  # Reason why I prefer python for quick scatches... basically everything works just fine
  x1, y1, x2, y2 = line.split(" ")

  # Technically, the input here currently is a string unless we convert it to a number, which is highly recommended for euklidian distance
  line = Line(Point(float(x1), float(y1)), Point(float(x2), float(y2)))

  # Personaly, I would build a 
  plt.plot([x1, x2], [y1, y2], marker='o')
  print(f'{x1} {y1} {x2} {y2}')
plt.show()
