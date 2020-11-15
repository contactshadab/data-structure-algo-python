'''
https://leetcode.com/problems/add-binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
'''


# Solution 1
# The naive approach is to convert both strings into integer and add them. Return the result by converting it back to binary
# Time complexity: O(n+m) where n is the length of first string and m is the length of second string
# Space complexity: O(1)
def add_binary_1(s1, s2):
    sum = int(s1, 2) + int(s2, 2)

    return '{0:b}'.format(sum)


# Solution 2
# Doing bit by bit computation
# Time complexity: O(max(n,m)) where n is the length of first string and m is the length of second string
# Space complexity: O(max(n,m)) to store the results
def add_binary_2(a, b):
    p1, p2 = len(a)-1, len(b)-1
    carry = 0
    result = []
    while p1 >= 0 or p2 >= 0:
        ch1 = a[p1] if p1 >= 0 else 0
        ch2 = b[p2] if p2 >= 0 else 0
        sum = int(ch1) + int(ch2) + carry
        if sum == 0 or sum == 1:
            result.append(str(sum))
            carry = 0
        elif sum == 2:
            result.append('0')
            carry = 1
        else:
            result.append('1')
            carry = 1

        p1 -= 1
        p2 -= 1

    if carry == 1:
        result.append('1')
    elif carry == 2:
        result.append('0')
        result.append('1')

    return ''.join(reversed(result))


# Solution 3
# Doing bit manipulation if sum is not allowed
# Time complexity: O(m+n) where n is the length of first string and m is the length of second string
# Space complexity: O(m+n)
def add_binary_3(a, b):
    x = int(a, 2)
    y = int(b, 2)
    while y != 0:
        without_carry = x ^ y
        carry = (x & y) << 1
        x, y = without_carry, carry

    return '{0:b}'.format(x)


if __name__ == "__main__":
    print(add_binary_1('1010', '1011'))
    print(add_binary_2('1010', '1011'))
    print(add_binary_3('1010', '1011'))
