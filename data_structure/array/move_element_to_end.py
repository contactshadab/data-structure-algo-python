'''
Source: AlgoExpert
You're given an array of integers and an integer. Write a function that moves
all instances of that integer in the array to the end of the array and returns
the array.


The function should perform this in place (i.e., it should mutate the input
array) and doesn't need to maintain the order of the other integers.

Input:  = [2, 1, 2, 2, 2, 3, 4, 2], to_move = 2
Output: [1, 3, 4, 2, 2, 2, 2, 2]
'''


def move_element_to_end(array, to_move):
    left = 0
    right = len(array) - 1
    while left < right:
        while left < right and array[left] != to_move:
            left += 1

        while left < right and array[right] == to_move:
            right -= 1

        array[left], array[right] = array[right], array[left]

    return array


if __name__ == "__main__":
    print(move_element_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2))
