'''
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''


# Run time complexity: O(log N)
# Space complexity: O(1)
def searchRange(nums, target):
    def search(left, right, searchLeft):
        index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                index = mid
                if searchLeft:
                    right = mid-1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return index

    left = search(0, len(nums)-1, True)
    if left > -1:
        right = search(left, len(nums)-1, False)
    else:
        right = -1

    return [left, right]


if __name__ == "__main__":
    print(searchRange([5, 7, 7, 8, 8, 10], 8))
