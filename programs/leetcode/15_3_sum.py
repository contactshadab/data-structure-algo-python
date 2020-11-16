'''
https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''


def three_sum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)-2):
        if i != 0 and nums[i-1] == nums[i]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            if left != i + 1 and nums[left-1] == nums[left]:
                left += 1
                continue

            sum = nums[i] + nums[left] + nums[right]
            if sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1

    return result
