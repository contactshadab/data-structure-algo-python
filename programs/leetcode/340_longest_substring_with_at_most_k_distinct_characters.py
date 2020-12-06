'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''


# Solution 1
# Run time complexity: O(NK)
# Space complexity: O(K)
def length_of_longest_substring_k_distinct(s, k):
    if len(s) == 0 or k == 0:
        return 0

    visited = {}
    left, right = 0, 0
    result = 1
    while right < len(s):
        visited[s[right]] = right

        if len(visited) == k+1:
            left_most = min(visited.values())
            del visited[s[left_most]]
            left = left_most + 1

        result = max(result, right - left + 1)
        right += 1

    return result


# Solution 2
# Run time complexity: O(N)
# Space complexity = O(K)
def length_of_longest_substring_k_distinct_2(s, k):
    from collections import OrderedDict
    if len(s) == 0 or k == 0:
        return 0

    visited = OrderedDict()
    left, right = 0, 0
    result = 1
    while right < len(s):
        # Remove item so that when we add it again it becomes the latest
        if s[right] in visited:
            del visited[s[right]]
        visited[s[right]] = right

        if len(visited) == k + 1:
            # get the leftmost distinct item index
            _, left_most = visited.popitem(last=False)
            left = left_most + 1

        result = max(result, right - left + 1)

        right += 1

    return result


if __name__ == "__main__":
    print(length_of_longest_substring_k_distinct("eceba", 2))
    print(length_of_longest_substring_k_distinct_2("eceba", 2))
