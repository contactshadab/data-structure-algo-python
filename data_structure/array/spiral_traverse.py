'''

'''


def spiral_traverse(array):
    result = []
    row_start, row_end = 0, len(array)-1
    col_start, col_end = 0, len(array[0])-1

    while row_start <= row_end and col_start <= col_end:
        for col in range(col_start, col_end+1):
            result.append(array[row_start][col])

        for row in range(row_start+1, row_end):
            result.append(array[row][col_end])

        if row_start == row_end:
            break

        for col in range(col_end, col_start-1, -1):
            result.append(array[row_end][col])

        if col_start == col_end:
            break

        for row in range(row_end-1, row_start, -1):
            result.append(array[row][col_start])

        row_start += 1
        row_end -= 1
        col_start += 1
        col_end -= 1

    return result


def spiral_traverse_recursive(array):
    return _spiral_traverse_recursive(
        array, 0, len(array)-1, 0, len(array[0])-1)


def _spiral_traverse_recursive(array, row_start, row_end, col_start, col_end):
    result = []
    if row_end < row_start or col_end < col_start:
        return []

    for col in range(col_start, col_end+1):
        result.append(array[row_start][col])

    for row in range(row_start+1, row_end):
        result.append(array[row][col_end])

    if row_start == row_end:
        return result

    for col in range(col_end, col_start-1, -1):
        result.append(array[row_end][col])

    if col_start == col_end:
        return result

    for row in range(row_end-1, row_start, -1):
        result.append(array[row][col_start])

    return result + _spiral_traverse_recursive(
        array, row_start+1, row_end-1, col_start+1, col_end-1)


if __name__ == "__main__":
    array = [
        [1,   2,  3, 4],
        [12, 13, 14, 5],
        [11, 16, 15, 6],
        [10,  9,  8, 7],
    ]

    result = spiral_traverse(array)
    print(result)
    print(spiral_traverse_recursive(array))
