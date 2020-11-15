'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

'''


def subarray_sum(nums, k):
    sum = {}
    count = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        if current_sum == k:
            count += 1

        if (current_sum - k) in sum:
            count += sum[current_sum - k]

        sum[current_sum] = sum[current_sum] + 1 if (current_sum) in sum else 1

    return count


if __name__ == "__main__":
    print(subarray_sum([1, 2, 3], 3))
