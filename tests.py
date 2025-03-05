import unittest

from maze import Maze


class Tests(unittest.TestCase):

    #Initial test
    def test_maze_create_cells(self):
        #Test a generic maze
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )


    #Test initialization with different sizes
    def test_maze_different_sizes(self):
        # Test a small maze
        m1 = Maze(0, 0, 5, 5, 10, 10) 
        self.assertEqual(len(m1._cells), 5) 
        self.assertEqual(len(m1._cells[0]), 5) 
        
        # Test a larger maze
        m2 = Maze(0, 0, 15, 20, 10, 10) 
        self.assertEqual(len(m2._cells), 15)  
        self.assertEqual(len(m2._cells[0]), 20) 


    #Test initialization within the maze
    def test_cell_initialization(self):
        m = Maze(0, 0, 3, 3, 10, 10)
        
        # Check if all cells have walls
        for i in range(3):
            for j in range(3):
                cell = m._cells[i][j]
                self.assertTrue(cell.has_left_wall)
                self.assertTrue(cell.has_right_wall)
                self.assertTrue(cell.has_top_wall)
                self.assertTrue(cell.has_bottom_wall)
                
                # Check that win parameter was passed correctly
                self.assertIsNone(cell._win)


    #Test with Window parameter being optional
    def test_window_parameter_optional(self):
        try:
            m = Maze(0, 0, 5, 5, 10, 10, None)
            # Check that window is None
            self.assertIsNone(m._win)  
        except Exception as e:
            self.fail(f"Creating maze without window raised exception: {e}")


    #Test cells calculate correct dimensions
    def test_cell_dimensions(self):
        cell_size_x = 15
        cell_size_y = 20
        m = Maze(0, 0, 3, 4, cell_size_x, cell_size_y)
        
        # Test that maze stores the correct cell sizes
        self.assertEqual(m._cell_size_x, cell_size_x)
        self.assertEqual(m._cell_size_y, cell_size_y)


    #Test _break_enterance_and_exit method
    def test_break_entrance_and_exit(self):
        #Create a small maze (e.g., 2x2 or 3x3).
        m = Maze(0, 0, 3, 3, 10, 10)

        #Call the method to break entrance and exit walls.
        m._break_entrance_and_exit()

        #Assert that the top wall of the top-left cell is False.
        assert m._cells[0][0].has_top_wall == False

        #Assert that the bottom wall of the bottom-right cell is False.
        assert m._cells[-1][-1].has_bottom_wall == False

    
    #Test the _reset_cells_visited method
    def test_reset_cells_visited(self):
        #Create a small maze (e.g., 2x2 or 3x3).
        m = Maze(0, 0, 3, 3, 10, 10)

        #Simulate some cells being marked as visited.
        for row in m._cells:
            for col in row:
                col.visited = True

        #Ensure all cells were initially marked as visited.
        for row in m._cells:
            for col in row:
                self.assertTrue(col.visited)        

        #Reset each cell's visited value to False
        m._reset_cells_visited()

        #Validate each cells visited value
        for row in m._cells:
            for col in row:
                self.assertFalse(col.visited)


if __name__ == "__main__":
    unittest.main()