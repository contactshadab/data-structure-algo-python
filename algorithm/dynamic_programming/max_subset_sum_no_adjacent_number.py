'''
 Write a function that takes in an array of positive integers and returns the maximum sum of non-adjacent elements in the array. 
 If a sum can't be generated, the function should return 0
 Input = [75, 105, 120, 75, 90, 135] 
 Output = 330
'''


# Solution 1
# Run time complexity: O(n)
# Space complexity: O(n)
def max_subset_sum_no_adjacent_1(array):
    if array is None or len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    max_sum = [None for i in range(len(array))]
    max_sum[0] = array[0]
    max_sum[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2]+array[i])

    return max_sum[-1]


# Solution 2
# Run time complexity: O(n)
# Space complexity: O(1)
def max_subset_sum_no_adjacent_2(array):
    if array is None or len(array) == 0:
        return 0

    if len(array) == 1:
        return array[0]

    max_sum = [None for i in range(len(array))]
    max_sum[0] = array[0]
    max_sum[1] = max(array[0], array[1])

    for i in range(2, len(array)):
        max_sum[i] = max(max_sum[i-1], max_sum[i-2]+array[i])

    return max_sum[-1]


if __name__ == "__main__":
    array = [75, 105, 120, 75, 90, 135]
    print(max_subset_sum_no_adjacent_1(array))
    print(max_subset_sum_no_adjacent_2(array))
