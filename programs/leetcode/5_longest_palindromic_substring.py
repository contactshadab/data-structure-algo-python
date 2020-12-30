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


# Solution 2: DP
# Run time complexity: O(n^2)
# Space complexity: O(n^2)
def longest_palindrome_dp(s):
    n = len(s)
    dp = [[None for j in range(n)] for i in range(n)]

    start = 0
    length = 1

    # Calculate dp table for all substrings of length greater than 2
    for l in range(1, n+1):
        i = 0
        while i < n - l + 1:
            j = i + l - 1
            if l == 1:
                dp[i][i] = True
                if l > length:
                    start = i
                    length = l
            elif l == 2:
                if s[i] == s[j]:
                    dp[i][i+1] = True
                    if l > length:
                        start = i
                        length = l
            else:
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if l > length:
                        start = i
                        length = l
                else:
                    dp[i+1][j-1] = False

            i += 1

    return s[start: start+length]
