'''
https://leetcode.com/problems/search-in-rotated-sorted-array/
33. Search in Rotated Sorted Array

You are given an integer array nums sorted in ascending order, and an integer target.

Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

If target is found in the array return its index, otherwise, return -1.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guranteed to be rotated at some pivot.
-10^4 <= target <= 10^4

'''


# Run time complexity: O(log n)
# Space Complexity: O(1)
def search(nums, target):

    def findRotationIndex():
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return left

    def binarysearch(left, right):
        while left <= right:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    if len(nums) == 1:
        return 0 if nums[0] == target else -1

    rotation_index = findRotationIndex()

    if target >= nums[rotation_index] and target <= nums[len(nums)-1]:
        return binarysearch(rotation_index, len(nums)-1)
    else:
        return binarysearch(0, rotation_index)


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
