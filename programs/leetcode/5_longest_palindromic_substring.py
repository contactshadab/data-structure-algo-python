'''
https://leetcode.com/problems/longest-palindromic-substring/
5. Longest Palindromic Substring
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
Example 3:

Input: s = "a"
Output: "a"
Example 4:

Input: s = "ac"
Output: "a"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
'''


# Run time complexity: O(n^2)
# Space complexity: O(1)
def longestPalindrome(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left+1: right]

    longest = ""
    for i in range(len(s)):
        odd = expand(i, i)
        if len(odd) > len(longest):
            longest = odd

        even = expand(i, i+1)
        if len(even) > len(longest):
            longest = even

    return longest
