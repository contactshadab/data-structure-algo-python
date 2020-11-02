'''
Source: AlgoExpert

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.

Note that the target sum has to be obtained by summing two different integers
in the array; you can't add a single integer to itself in order to obtain the
target sum.

Input: array = [3, 5, -4, 8, 11, 1, -1, 6], targetSum=10
Output: [-1, 11]

'''

# Solution 1
# Run time complexity: O(n^2), Space complexity: O(1)


def two_number_sum_1(array, targetSum):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]

    return []

# Solution 2
# Run time complexity: O(n), Space complexity: O(n)


def two_number_sum_2(array, targetSum):
    seen = set()
    for num in array:
        target = targetSum - num
        if target in seen:
            return [target, num]

        seen.add(num)

    return []

# Solution 3
# Run time complexity: O(nlog(n)), Space complexity: O(1)


def two_number_sum_3(array, targetSum):
    array.sort()
    left = 0
    right = len(array)-1

    while left < right:
        sum = array[left] + array[right]
        if sum == targetSum:
            return [array[left], array[right]]

        if sum > targetSum:
            right -= 1
        else:
            left += 1

    return []


if __name__ == "__main__":
    print(two_number_sum_1([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_number_sum_2([3, 5, -4, 8, 11, 1, -1, 6], 10))
    print(two_number_sum_3([3, 5, -4, 8, 11, 1, -1, 6], 10))
