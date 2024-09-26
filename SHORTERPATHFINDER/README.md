Maze Pathfinding with Python and Curses
This project is a simple maze-solving program written in Python using the curses library. It visualizes a pathfinding algorithm that navigates through a maze to find a path from a start point (S) to an end point (E).

Features
Hard Maze: The maze is designed to be more complex, with multiple paths and dead-ends.
Path Visualization: The program visually displays the path taken from start to end in real-time using the terminal.
Breadth-First Search (BFS): The maze is solved using a BFS approach to ensure that the shortest path is found.
Prerequisites
To run this project, you need to have Python installed and the following package(s) based on your platform:

Windows
Install the windows-curses package (since curses is not natively available on Windows):
bash
Copy code
pip install windows-curses
Linux / macOS
No additional installation is needed, as curses is built into the system's Python installation.

How to Run
Clone or download the project.
Open your terminal and navigate to the project directory.
Run the Python script using the following command:
bash
Copy code
python maze_solver.py
The maze will be displayed in your terminal, and the path from the start (S) to the end (E) will be highlighted in real-time.

Code Explanation
Maze Layout (complex_maze): The maze is represented as a 2D list where:

# represents walls.
S is the starting point.
E is the ending point.
" " (spaces) represent the open path where the algorithm can move.
Functions:

show_maze: Visualizes the maze and the current path.
get_start_position: Finds the start position (S) in the maze.
find_neighbors: Identifies the neighboring cells that can be explored (up, down, left, right).
search_maze_path: Implements BFS to explore the maze and find the shortest path.
run_maze: The main function that sets up the screen and runs the maze-solving algorithm.
Example Output
As the program runs, you'll see the path taken by the algorithm visualized in real-time with the maze grid updating in the terminal.

Contribution
Feel free to modify the maze or the pathfinding logic to explore more complex algorithms or different maze layouts. Pull requests are welcome!