'''

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
'''


def multiply(num1, num2):
    num1 = convert_to_int(num1)
    num2 = convert_to_int(num2)
    return convert_to_string(num1 * num2)


def convert_to_int(s):
    num = 0
    for i in range(len(s)-1, -1, -1):
        num += int(s[i]) * (10 ** (len(s)-1-i))

    return num


def convert_to_string(num):
    s = []
    while num >= 10:
        reminder = num % 10
        s.append(chr(ord('0') + reminder))
        num = num // 10

    s.append(chr(ord('0') + num))

    return ''.join(reversed(s))


if __name__ == "__main__":
    print(multiply('123', '20'))
