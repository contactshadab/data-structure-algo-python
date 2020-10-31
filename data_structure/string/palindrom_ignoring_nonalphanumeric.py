'''
Source: Leetcode 125. Valid Palindrome
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
'''


def is_palindrome(s: str) -> bool:
    if s is None or len(s) <= 1:
        return True

    left = 0
    right = len(s)-1

    while left <= right:
        if not s[left].isalnum():
            left += 1
            continue

        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("a,bb! a"))  # True
    print(is_palindrome("ab c b@a"))  # True
    print(is_palindrome(""))  # True
    print(is_palindrome("abca"))  # False
