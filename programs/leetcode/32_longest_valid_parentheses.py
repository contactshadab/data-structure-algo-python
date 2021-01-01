'''
https://leetcode.com/problems/longest-valid-parentheses/
32. Longest Valid Parentheses
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

'''


# Run time complexity: O(n)
# Space complexity: O(n)
def longestValidParentheses(s):
    if not s:
        return 0

    stack = [-1]
    longest = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            l = i - stack[-1]
            longest = max(longest, l)

    return longest
