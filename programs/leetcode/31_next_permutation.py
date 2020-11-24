'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
Example 4:

Input: nums = [1]
Output: [1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
'''


# Runtime complexity: O(n), Space complexity: O(1)
def next_permutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    i = len(nums) - 1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    if i > 0:
        j = len(nums)-1
        while j >= i and nums[j] <= nums[i-1]:
            j -= 1

        # If we are here we found a number just greater than i-1th index number
        # Swap them
        nums[i-1], nums[j] = nums[j], nums[i-1]
        # Reverse the subarray from ith position till end.
        # All nums from i will be in decreasing order
        reverse(nums, i)
    else:
        # Since we cannot find a valid pair with nums[i-1] < nums[i]
        # Therefore the array is sorted in decreasing order. REverse it as its requirement
        reverse(nums, 0)


def reverse(self, nums, start):
    end = len(nums)-1
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    nums = [3, 2, 1]
    next_permutation(nums)
    print(nums)
