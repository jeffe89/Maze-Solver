# Maze Solver

## Overview
This project is a **maze solver** that generates and solves mazes using Python. The solver uses **Depth-First Search (DFS)** to navigate through a randomly generated maze, visualizing the solution with a graphical interface using **Tkinter**.

## Screenshot
![Maze Solver Screenshot](https://github.com/jeffe89/Maze-Solver/blob/main/Maze%20Solver%20Screenshot.png)

## Installation & Usage
### Prerequisites
- Python 3.x
- Tkinter (for graphical display)

### Installing Tkinter
Tkinter is included with standard Python distributions, but if needed, install it using:
- **Windows & macOS:** Tkinter is pre-installed.
- **Linux:** Install using:
  ```sh
  sudo apt-get install python3-tk
  ```

### Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/jeffe89/Maze-Solver.git
   ```
2. Navigate into the project directory:
   ```sh
   cd Maze-Solver
   ```
3. Run the solver:
   ```sh
   python main.py
   ```

## Project Structure
```
maze-solver/
├── main.py          # Entry point to run the maze solver
├── maze.py          # Defines the maze structure
├── cell.py          # Represents individual maze cells
├── graphics.py      # Handles graphical rendering of the maze
├── tests.py         # Unit tests for the maze solver
├── LICENSE          # Project license
├── README.md        # Documentation (this file)
```

## Detailed File and Method Descriptions

### `main.py`
This is the entry point of the program. It initializes the maze, runs the solver using DFS, and displays the solution using the graphics module.
- `main()`: Initializes and executes the maze solver.

### `maze.py`
Defines the maze structure, including generation and solving.
- `class Maze`: Represents the maze grid and contains methods for generating and solving it.
  - `__init__`: Initializes a maze of given dimensions.
  - `_create_cells`: Creates the grid of maze cells.
  - `_draw_cell`: Draws an individual maze cell.
  - `_animate`: Handles animation updates during maze generation and solving.
  - `_break_entrance_and_exit`: Removes walls at the start and end of the maze.
  - `_break_walls_r`: Recursively removes walls to create a solvable maze.
  - `_reset_cells_visited`: Resets the visited state of all cells before solving.
  - `_solve`: Initiates the DFS-based solution process.
  - `_solve_r`: Recursive DFS function to solve the maze.

### `cell.py`
Defines individual cells within the maze.
- `class Cell`: Represents a single cell in the maze.
  - `__init__`: Initializes the cell with its coordinates.
  - `draw`: Draws the cell on the graphical interface.
  - `draw_move`: Animates movement from one cell to another.

### `graphics.py`
Handles visualization of the maze and solution path.
- `class Window`: Manages the GUI window.
  - `__init__`: Initializes the graphical window.
  - `redraw`: Refreshes the display.
  - `wait_for_close`: Waits for the user to close the window.
  - `draw_line`: Draws a line on the graphical window.
  - `close`: Closes the window.
- `class Point`: Represents a point in the graphical space.
  - `__init__`: Initializes the point with coordinates.
- `class Line`: Represents a line in the graphical space.
  - `__init__`: Initializes a line with start and end points.
  - `draw`: Draws the line in the window.

### `tests.py`
Contains unit tests for verifying the correctness of the maze generation and solving algorithms.
- `test_maze_create_cells()`: Validates the proper creation of maze cells.
- `test_maze_different_sizes()`: Ensures different maze sizes generate correctly.
- `test_cell_initialization()`: Verifies that cells are initialized properly.
- `test_window_parameter_optional()`: Tests if window parameters have default values.
- `test_cell_dimensions()`: Checks if cells maintain correct dimensions.
- `test_break_entrance_and_exit()`: Confirms entrance and exit are correctly broken.
- `test_reset_cells_visited()`: Ensures cells' visited status resets correctly before solving.

## Author

Geoffrey Giordano

## License
This project is licensed under the terms specified in the `LICENSE` file.

## Contributing
Contributions are welcome! Feel free to fork the repo and submit a pull request.
