'''
https://leetcode.com/problems/intersection-of-two-arrays/
349. Intersection of Two Arrays
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''


# Run time complexity: O(N+M)
# Space complexity: O(N+M)
def intersection(nums1, nums2):
    set1 = set(nums1)

    result = set()
    for num in nums2:
        if num in set1:
            result.add(num)

    return list(result)


# Assume both list are sorted
# Run tiem complexity: O(N+M)
# Space complexity: O(1)
def intersection_if_sorted_lists(nums1, nums2):
    first, second = 0, 0
    result = set()
    while first < len(nums1) and second < len(nums2):
        if nums1[first] == nums2[second]:
            result.add(nums1[first])
            first += 1
            second += 1
        elif nums1[first] > nums2[second]:
            second += 1
        else:
            first += 1

    return list(result)


if __name__ == "__main__":
    print(intersection([1, 2, 2, 1], [2, 2]))
    print(intersection_if_sorted_lists([1, 1, 2, 2], [2, 2]))
    print(intersection_if_sorted_lists([], [2, 2]))
    print(intersection_if_sorted_lists([1, 1, 2, 2], []))
