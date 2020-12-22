'''
https://leetcode.com/problems/regular-expression-matching/
10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where: 

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''


def isMatch(s, p):
    if not p:
        return True if not s else False

    first_match = s and p[0] in [s[0], '.']

    if len(p) > 1 and p[1] == '*':
        # If next char is wildcard, we have two choices - ignore this pattern or include this pattern
        return isMatch(s, p[2:]) or first_match and isMatch(s[1:], p)
    else:
        return first_match and isMatch(s[1:], p[1:])
