import curses
from curses import wrapper
import queue
import time

# Harder maze layout
complex_maze = [
    ["#", "S", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", " ", "#", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", "#", "#", " ", "#", "#"],
    ["#", " ", " ", " ", " ", " ", "#", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "E", "#"]
]

# Display the maze with the path (route) if any
def show_maze(maze, screen, route=[]):
    color_path = curses.color_pair(1)
    color_maze = curses.color_pair(2)

    for row_num, row in enumerate(maze):
        for col_num, value in enumerate(row):
            if (row_num, col_num) in route:  # If the cell is in the path, mark it
                screen.addstr(row_num, col_num * 2, "X", color_path)
            else:  # Otherwise, print the maze layout
                screen.addstr(row_num, col_num * 2, value, color_maze)

# Find the start position in the maze ('S')
def get_start_position(maze):
    for row_num, row in enumerate(maze):
        for col_num, value in enumerate(row):
            if value == "S":  # 'S' is the start point
                return row_num, col_num

# Explore neighbors of a position in the maze
def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors

# Find a path from start to end
def search_maze_path(maze, screen):
    start_char = "S"
    end_char = "E"
    start_position = get_start_position(maze)

    path_queue = queue.Queue()  # Queue to hold positions to explore
    path_queue.put((start_position, [start_position]))

    visited_positions = set()  # Track visited positions

    while not path_queue.empty():
        current_position, current_path = path_queue.get()
        row, col = current_position

        screen.clear()  # Clear screen and display the updated maze
        show_maze(maze, screen, current_path)
        time.sleep(0.1)
        screen.refresh()

        if maze[row][col] == end_char:  # Check if we reached the end
            return current_path

        # Explore neighbors (UP, DOWN, LEFT, RIGHT)
        for neighbor in find_neighbors(maze, row, col):
            if neighbor in visited_positions:
                continue

            neighbor_row, neighbor_col = neighbor
            if maze[neighbor_row][neighbor_col] == "#":  # Wall
                continue

            new_path = current_path + [neighbor]  # Add new position to path
            path_queue.put((neighbor, new_path))  # Put it in queue
            visited_positions.add(neighbor)

# Main function to run the maze search
def run_maze(screen):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Path color
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Maze color

    search_maze_path(complex_maze, screen)
    screen.getch()  # Wait for user input

# Start the program
wrapper(run_maze)
