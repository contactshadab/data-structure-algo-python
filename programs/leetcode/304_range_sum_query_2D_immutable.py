'''
https://leetcode.com/problems/range-sum-query-2d-immutable/
304. Range Sum Query 2D - Immutable
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Example:

Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:

You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''


# Solution 2:
# Run time complexity: O(m*n), everytime sum_region is called
# Space complexity: O(1)
def sum_region(row1, col1, row2, col2):
    sum = 0
    for row in range(row1, row2+1):
        for col in range(col1, col2+1):
            sum += self.matrix[row][col]

    return sum


# Solution 2:
# Run time complexityy: Precalculate sum of all cells in every row. O(M*N). Each query will take O(M)
# Space complexity: O(M*N)
class SumRegion:
    def __init__(self):
        if not matrix:
            return

        # Precalculate sum of all cells in every row. O(M*N)
        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0 for col in range(cols+1)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                self.dp[row][col+1] = matrix[row][col] + self.dp[row][col]

    # Each call to sum_region will take O(M)
    def sum_region(self, row1, col1, row2, col2):
        sum = 0
        for row in range(row1, row2+1):
            sum = sum + self.dp[row][col2+1] - self.dp[row][col1]

        return sum


# Solution 3
# Run time complexity: Pre computation O(M*N). Each query O(1)
# Space complexity: O(M*N)
class NumMatrix:

    def __init__(self, matrix):
        if not matrix:
            return

        self.matrix = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        self.dp = [[0 for col in range(cols+1)] for row in range(rows+1)]

        # Commulitive sum from origin
        for row in range(1, rows+1):
            for col in range(1, cols+1):
                current = self.matrix[row-1][col-1]
                self.dp[row][col] = current + self.dp[row-1][col] + \
                    self.dp[row][col-1] - self.dp[row-1][col-1]

    def sumRegion(self, row1, col1, row2, col2):
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        sum = self.dp[row2][col2] - self.dp[row1-1][col2] - \
            self.dp[row2][col1-1] + self.dp[row1-1][col1-1]

        return sum
