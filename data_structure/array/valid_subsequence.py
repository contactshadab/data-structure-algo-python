'''
Source: AlgoExpert

Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.


A subsequence of an array is a set of numbers that aren't necessarily adjacent
in the array but that are in the same order as they appear in the array. For
instance, the numbers [1, 3, 4]  form a subsequence of the array
[1, 2, 3, 4] , and so do the numbers [2, 4]

Note
that a single number in an array and the array itself are both valid
subsequences of the array.
'''


def is_valid_subsequence(array, sequence):
    p = 0
    for item in array:
        if p == len(sequence):
            return True

        if item == sequence[p]:
            p += 1

    return p == len(sequence)


if __name__ == "__main__":
    print(is_valid_subsequence([1, 2, 3, 4], [1, 3, 4]))
    print(is_valid_subsequence([1, 2, 3, 4], [1, 3, 4, 2]))
