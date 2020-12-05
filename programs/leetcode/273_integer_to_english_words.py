'''
https://leetcode.com/problems/integer-to-english-words/
273. Integer to English Words
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
 

Constraints:

0 <= num <= 231 - 1

'''


def number_to_words(num):
    def one(num):
        dict = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
                5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        return dict[num]

    def two(num):
        less_than_20 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                        15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        tens = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty',
                60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        if num < 10:
            return one(num)
        if num < 20:
            return less_than_20[num]
        else:
            rest = num % 10
            return tens[(num // 10) * 10] + ' ' + one(num % 10) if rest else tens[(num // 10) * 10]

    def three(num):
        hundreds = num // 100
        rest = num - hundreds * 100

        if hundreds and rest:
            return one(hundreds) + ' Hundred ' + two(rest)
        elif hundreds and not rest:
            return one(hundreds) + ' Hundred'
        elif not hundreds and rest:
            return two(rest)
        else:
            return ''

    if not num:
        return 'Zero'

    billions = num // 1000000000
    rest = num - billions * 1000000000
    millions = rest // 1000000
    rest = rest - millions * 1000000
    thousands = rest // 1000
    rest = rest - thousands * 1000

    result = ''
    if billions:
        if result:
            result += ' '
        result = three(billions) + ' Billion'

    if millions:
        if result:
            result += ' '
        result += three(millions) + ' Million'

    if thousands:
        if result:
            result += ' '
        result += three(thousands) + ' Thousand'

    if rest:
        if result:
            result += ' '
        result += three(rest)

    return result


if __name__ == "__main__":
    print(number_to_words(123))
