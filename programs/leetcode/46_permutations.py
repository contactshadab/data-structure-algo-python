'''
https://leetcode.com/problems/permutations/
46. Permutations
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
'''


def permute(nums):
    def backtrack(position):
        if position == len(nums):
            permutations.append(nums[:])
            return

        for i in range(position, len(nums)):
            # Swap the ith item to the position we are currently aiming to fill slot for
            nums[position], nums[i] = nums[i], nums[position]
            backtrack(position + 1)
            # Swap back to backtrack with new permutation
            nums[position], nums[i] = nums[i], nums[position]

    permutations = []
    backtrack(0)
    return permutations


if __name__ == "__main__":
    print(permute([1, 2, 3]))
