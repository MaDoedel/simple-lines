# Simple-line

As part of a submission, this project contains a Python script that offers a possible solution approach as a proof of concept, alongside the Java project implementation as the final solution.

## Task

Given a list of coordinate pairs representing the start and end points of lines, two lines can be combined into a single line if one of the endpoints of one line matches an endpoint of another line. If more than two lines meet at a point, no combination occurs at that point. The input file contains one line per line segment, with each line containing four floating-point numbers separated by spaces, representing the coordinates \(X1\), \(Y1\), \(X2\), and \(Y2\).

## Expectations

Through this proof of concept, the input graph is refined into a star composed of three line segments.

![Initial Plot](/initial_plot.png)
![Reworked Plot](/reworked_plot.png)

Lengths: 1565.53, 965.49, 636.06

## Thoughts

As this task is rather straightforward, I prioritized a lightweight implementation without unnecessary complications from design patterns that might add variability or advanced parsing technologies. However, considerations of specific patterns and arguments are communicated through comments.

## Software Stack

As the interviewer suggested a tendency towards adapting frontend technologies and libraries as a backend developer, I would brand this project as a React-driven. Thus, a lightweight Java web framework as the backend (for a single GET request), combined with ReactJS, should suit the needs.

## Main Function

The main function performs the following steps:

1. **Read the Input File**: The input file is read from the `src/main/resources` directory, and each line is parsed to extract the coordinates of the line segments.
2. **Build the Adjacency List**: An adjacency list is constructed to represent the graph of line segments.
3. **Traverse the Line Segments**: The line segments are traversed to identify and combine segments that can be merged based on the given criteria.
4. **Print the Lengths**: The lengths of the resulting line segments are calculated and printed.
5. **Draw the Line Segments**: The final line segments are drawn and displayed.

### Example Usage

To run the main function, use the following command:

#### Linux
```sh
./gradlew run
```

#### Windows
```sh
gradlew.bat run
```