'''
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
'''


def min_remove_to_make_valid(s) -> str:
    result = []
    opening = 0
    for ch in s:
        if ch == '(':
            opening += 1
        elif ch == ')':
            opening -= 1
        else:
            result.append(ch)
            continue

        if opening >= 0:
            result.append(ch)
        else:
            opening += 1

    for i in range(len(result)-1, -1, -1):
        if opening <= 0:
            break

        if result[i] == '(':
            result[i] = ''
            opening -= 1

    return ''.join(result)


if __name__ == "__main__":
    print(min_remove_to_make_valid("lee(t(c)o)de)"))
