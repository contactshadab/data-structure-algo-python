'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''


# Run time complexity: O(3 ^ M * 4 ^ M), where is M is the no of digits mapping to 3 characters and M mapping to 4 characters
# Space complexity: O(3 ^ M * 4 ^ M), to store the mapping
def letter_combinations(digits):

    letters = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def backtrack(combination, next_digits):
        if len(next_digits) == 0:
            result.append(combination)
            return

        current = next_digits[0]
        for letter in letters[current]:
            backtrack(combination + letter, next_digits[1:])

    result = []
    if not digits:
        return []

    backtrack('', digits)
    return result


if __name__ == "__main__":
    print(letter_combinations('23'))
