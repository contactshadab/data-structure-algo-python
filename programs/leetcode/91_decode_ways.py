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


# Solution 1: Recursive
# Run time complexity: O(n)
# Space complexity: O(n)
def num_decodings(s):
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

    memo = {}

    return _num_decodings(s, 0)


# Solution 2: Recursive (starting at the end)
# Run time complexity: O(n)
# Space complexity: O(n)
def num_decodings_2(s):
    def decode(i):
        if i in memoise:
            return memoise[i]

        if i < 0:
            return 1

        if i == 0:
            return 1 if s[0] != '0' else 0

        # Decode one digit, i
        one = decode(i-1) if s[i] != '0' else 0

        # Decode two digits, i and i-1
        two = decode(i-2) if s[i-1] != '0' and int(s[i-1:i+1]) <= 26 else 0
        memoise[i] = one + two
        return one + two

    if s is None or len(s) == 0:
        return 0

    memoise = {}

    return decode(len(s)-1)


# Solution 3: DP
# Run time complexity: O(n)
# Space complexity: O(1)
def num_decodings_3(s):
    if s is None or len(s) == 0:
        return 0

    # Initialise the dp array
    dp = [None for i in range(len(s) + 1)]
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, len(dp)):
        ways = 0
        if s[i-1] != '0':
            ways = dp[i-1]

        if s[i-2] != '0' and int(s[i-2:i]) <= 26:
            ways += dp[i-2]

        dp[i] = ways

    return dp[-1]


if __name__ == "__main__":
    print(num_decodings("226"))
    print(num_decodings_2("226"))
