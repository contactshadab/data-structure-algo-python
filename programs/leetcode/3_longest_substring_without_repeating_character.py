'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


def longest_substring(s):
    if s is None:
        raise Exception('Empty string')

    if len(s) < 1:
        return 0

    start = 0
    current = 1
    longest = 1
    seen = {s[0]: 0}

    while start < len(s) and current < len(s):
        if s[current] in seen:
            longest = max(longest, current - start)
            start = seen[s[current]] + 1
        else:
            longest = max(longest, current - start + 1)

        seen[s[current]] = current
        current += 1

    return longest


if __name__ == "__main__":
    print(longest_substring("abcabcbb"))
    print(longest_substring("bbbbb"))
    print(longest_substring("pwwkew"))
    print(longest_substring(""))
