#!/usr/bin/python3
"""Create a function def island_perimeter(grid): that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water

There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

Args:
    grid: rectangular, with its width and height not exceeding 100

Return:
    Perimeter: 
    """

def is_water(cell_value):
    """Check if a cell represents water (0).

    Args:
        cell_value (int): Value of the grid cell.

    Returns:
        int: 1 if the cell is water (0), otherwise 0.
    """
    if cell_value == 0:
        return 1
    return 0


def island_perimeter(grid):
    """
    A function that  returns the perimeter of the island described in grid
    """
        # Get the dimensions of the grid
    num_rows = len(grid)
    num_cols = len(grid[0]) if num_rows > 0 else 0  # Ensure grid has columns

    # Validate grid dimensions
    assert 1 <= num_rows <= 100 and 1 <= num_cols <= 100, "Grid dimensions must be between 1 and 100"

    perimeter = 0

    # Iterate over each cell in the grid
    for i in range(num_rows):
        for j in range(num_cols):
            # Validate grid values (must be 0 or 1)
            assert grid[i][j] in [0, 1], "Grid values must be 0 or 1"

            if grid[i][j] == 1:  # Found part of the island
                # Check adjacent cells for water (0) or boundary
                if i - 1 < 0:  # Check above cell
                    perimeter += 1
                else:
                    perimeter += is_water(grid[i-1][j])

                if j - 1 < 0:  # Check left cell
                    perimeter += 1
                else:
                    perimeter += is_water(grid[i][j-1])

                if i + 1 >= num_rows:  # Check below cell
                    perimeter += 1
                else:
                    perimeter += is_water(grid[i+1][j])

                if j + 1 >= num_cols:  # Check right cell
                    perimeter += 1
                else:
                    perimeter += is_water(grid[i][j+1])

    return perimeter
