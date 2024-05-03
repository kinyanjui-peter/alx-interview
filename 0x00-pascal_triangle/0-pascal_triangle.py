#!/usr/bin/python3
"""A script to determine Pascal's triangle for any number of rows"""


def pascal_triangle(n):
  """
  Generate Pascal's triangle for a given number of rows (n).

  Parameters:
  n (int): Number of rows for Pascal's triangle.

  Returns:
  list of lists of integers: Pascal's triangle as a list of lists.
                              Each inner list represents a row of the triangle.
  """
  triangle = []

  if n <= 0:
    return triangle  # Return empty triangle for non-positive n

  for i in range(n):
    temp_list = []

    for j in range(i + 1):
      if j == 0 or j == i:
        temp_list.append(1)
      else:
        # Calculate element using values from the previous row
        element = triangle[i - 1][j - 1] + triangle[i - 1][j]
        temp_list.append(element)

    triangle.append(temp_list)

  return triangle


# Example usage:
if __name__ == "__main__":
  num_rows = 5  # Specify the number of rows for Pascal's triangle
  result = pascal_triangle(num_rows)
  print(result)