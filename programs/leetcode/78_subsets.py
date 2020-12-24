'''
https://leetcode.com/problems/subsets/
78. Subsets
Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
'''


# The time and space complexity for all three approaches is the same
# Time complexity: O(n*2^n), 2^n is the total no of subsets while each subset copy operation takes O(n)
# Space complexity: O(n*2^n), there will be 2^n subsets and each subset will take max n space
def subsets(nums):
    res = [[]]
    n = len(res)
    for num in nums:
        for item in res:
            res = res + [item + [num]]

    return res


def subsets_recursive(nums, i=None):
    if i is None:
        i = len(nums) - 1

    if i == -1:
        return [[]]

    subsets = subsets_recursive(nums, i-1)
    temp = []
    for subset in subsets:
        temp.append(subset + [nums[i]])
    subsets += temp

    return subsets


def subsets_backtracking(nums):
    def backtrack(start, comb):
        if len(comb) == length:
            res.append(comb[:])
            return

        for i in range(start, len(nums)):
            comb.append(nums[i])
            backtrack(i+1, comb)
            comb.pop()

    res = []
    for length in range(len(nums)+1):
        backtrack(0, [])
    return res
