'''
https://leetcode.com/problems/permutations-ii/
47. Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
'''


# Run time complexity: O(n* n!), worst case
# Space complexity: O(n!)
def permute(nums):
    def backtrack(slot):
        if slot == len(nums):
            perms.append(nums[:])
            return

        for option in options:
            if options[option] < 1:
                continue

            nums[slot] = option
            options[option] -= 1
            backtrack(slot + 1)
            options[option] += 1

    options = {}
    for num in nums:
        options[num] = options.get(num, 0)+1

    perms = []
    nums.sort()
    backtrack(0)
    return perms


if __name__ == "__main__":
    print(permute([1, 1, 2, 2]))
