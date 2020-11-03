'''
Source: AlgoExpert

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. The function should find all triplets in
the array that sum up to the target sum and return a two-dimensional array of
all these triplets. The numbers in each triplet should be ordered in ascending
order, and the triplets themselves should be ordered in ascending order with
respect to the numbers they hold.


If no three numbers sum up to the target sum, the function should return an
empty array.
Input [12, 3, 1, 2, -6, 5, -8, 6], Sum = 0
Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
'''


def three_number_sum(array, targetSum):
    array.sort()
    results = []
    for i in range(len(array)-2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            sum = array[i] + array[left] + array[right]
            if sum == targetSum:
                results.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif sum > targetSum:
                right -= 1
            else:
                left += 1
    return results


if __name__ == "__main__":
    print(three_number_sum([12, 3, 1, 2, -6, 5, -8, 6], 0))
