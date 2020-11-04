'''
Source: AlgoExpert
Write a function that takes in two non-empty arrays of integers, finds the
pair of numbers (one from each array) whose absolute difference is closest to
zero, and returns an array containing these two numbers, with the number from
the first array in the first position.

Note that the absolute difference of two integers is the distance between
them on the real number line. For example, the absolute difference of -5 and 5
is 10, and the absolute difference of -5 and -4 is 1.

You can assume that there will only be one pair of numbers with the smallest
difference.
Input: arrayOne = [-1, 5, 10, 20, 28, 3], arrayTwo = [26, 134, 135, 15, 17]
Output: [28, 26]
'''


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    p1 = 0
    p2 = 0

    result = [arrayOne[0], arrayTwo[0]]
    min_distance = abs(arrayOne[0] - arrayTwo[0])
    while p1 < len(arrayOne) and p2 < len(arrayTwo):
        if arrayOne[p1] == arrayTwo[p2]:
            return [arrayOne[p1], arrayTwo[p2]]

        distance = abs(arrayOne[p1] - arrayTwo[p2])
        if distance < min_distance:
            min_distance = distance
            result = [arrayOne[p1], arrayTwo[p2]]

        if arrayOne[p1] < arrayTwo[p2]:
            p1 += 1
        else:
            p2 += 1

    return result


if __name__ == "__main__":
    one = [-1, 5, 10, 20, 28, 3]
    two = [26, 134, 135, 15, 17]
    print(smallestDifference(one, two))
