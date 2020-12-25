'''
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0

'''


def divide(dividend, divisor):
    MAX_INT = 2147483647  # 2**31 - 1
    MIN_INT = -2147483648  # -2**31
    HALF_MIN_INT = MIN_INT // 2

    # Handling overflow case for -2**31/-1
    if dividend == MIN_INT and divisor == -1:
        return MAX_INT

    positive = (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0)
    dividend = -dividend if dividend > 0 else dividend
    divisor = -divisor if divisor > 0 else divisor

    quotient = 0
    while dividend - divisor <= 0:
        poweroftwo = 1
        value = divisor
        while value > HALF_MIN_INT and value + value >= dividend:
            poweroftwo += poweroftwo
            value += value

        quotient += poweroftwo
        dividend -= value

    return quotient if positive else -quotient


if __name__ == "__main__":
    print(divide(9, 3))
