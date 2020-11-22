'''
https://leetcode.com/problems/roman-to-integer/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Example 2:

Input: s = "IV"
Output: 4
Example 3:

Input: s = "IX"
Output: 9
Example 4:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''


# Solution 1
# Traverse the string. If the next character is more significant than current character then substract them, else add them
# Time complexity: O(1) since max roman numeral make up 3999 so the characters will be finite
# Space complexity: O(1)

def roman_to_int_1(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    i = 0

    while i < len(s):
        if i+1 < len(s) and roman[s[i+1]] > roman[s[i]]:
            sum += roman[s[i+1]] - roman[s[i]]
            i += 2
        else:
            sum += roman[s[i]]
            i += 1

    return sum


# Solution 2
# Traverse the string righh to left. If the current character is of lesser value than the previous one, substract its value, else adds its value
# Time complexity: O(1) since max roman numeral make up 3999 so the characters will be finite
# Space complexity: O(1)
def roman_to_int_2(s):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    previous = s[len(s) - 1]
    sum = roman[previous]
    i = len(s) - 2

    while i >= 0:
        if roman[s[i]] > roman[previous]:
            sum += roman[s[i]]
        else:
            sum -= roman[s[i]]

        previous = s[i]
        i -= 1

    return sum


if __name__ == "__main__":
    print(roman_to_int_1("MCMXCIV"))
    print(roman_to_int_2("MCMXCIV"))
