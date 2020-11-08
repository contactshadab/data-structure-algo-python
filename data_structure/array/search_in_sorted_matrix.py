'''
You're given a two-dimensional array (a matrix) of distinct integers and a target integer.
Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width. 
Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1, -1]
'''


# Time complexity: O(m+n) where m is the number of rows and n is no of cols, Space complexity: O(1)
def search_in_sorted_matrix(matrix, target):
    row = 0
    col = len(matrix[0])-1
    while row < len(matrix) and col >= 0:
        elem = matrix[row][col]
        if target == elem:
            return [row, col]

        if target > elem:
            row += 1
        else:
            col -= 1

    return [-1, -1]


if __name__ == "__main__":
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004]
    ]

    print(search_in_sorted_matrix(matrix, 44))
    print(searchInSortedMatrix(matrix, 0))  # [-1, -1]
