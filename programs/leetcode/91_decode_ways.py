'''
https://leetcode.com/problems/decode-ways/
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

 

Example 1:

Input: s = "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "0"
Output: 0
Explanation: There is no character that is mapped to a number starting with '0'. We cannot ignore a zero when we face it while decoding. So, each '0' should be part of "10" --> 'J' or "20" --> 'T'.
Example 4:

Input: s = "1"
Output: 1
 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).
'''


memo = {}


def num_decodings(s):
    return _num_decodings(s, 0)


def isValid(num):
    return int(num) != 0 and int(num) <= 26


def _num_decodings(s, i):
    # If we reach the end of the string we successfully decoded it
    if i == len(s):
        return 1

    # String starting with 0 cant be decoded
    if s[i] == '0':
        return 0

    # If we are at the last position ands it is not 0 we decoded it successfully
    if i == len(s)-1:
        return 1

    if i in memo:
        return memo[i]

    ways = _num_decodings(
        s, i+1) + (_num_decodings(s, i+2) if isValid(s[i:i+2]) else 0)

    memo[i] = ways

    return ways


if __name__ == "__main__":
    print(num_decodings("226"))
