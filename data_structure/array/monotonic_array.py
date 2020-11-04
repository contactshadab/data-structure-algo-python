'''
Source: AlgoExpert
Write a function that takes in an array of integers and returns a boolean
representing whether the array is monotonic.

An array is said to be monotonic if its elements, from left to right, are
entirely non-increasing or entirely non-decreasing.

Note that empty arrays and arrays of one element are monotonic.
Input:  = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
Output: True
'''


def is_monotonic_1(array):
    if len(array) <= 2:
        return True

    direction = 0
    for i in range(1, len(array)):
        current_direction = array[i] - array[i-1]
        if direction == 0:
            direction = current_direction
            continue

        # Both direction and current_direction should have either positive or negative
        if direction * current_direction < 0:
            return False

    return True


def is_monotonic_2(array):
    if len(array) <= 2:
        return True

    direction_up = True
    direction_down = True

    for i in range(1, len(array)):
        direction = array[i] - array[i-1]
        if direction > 0:
            direction_down = False

        if direction < 0:
            direction_up = False

    return direction_down or direction_up


if __name__ == "__main__":
    print(is_monotonic_1([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
    print(is_monotonic_2([-1, -5, -10, -1100, -1100, -1101, -1102, -9001]))
