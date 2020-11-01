'''
Source: AlgoExpert

Write a function that, given a string, returns its longest palindromic
substring.

A palindrome is defined as a string that's written the same forward and
backward. Note that single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.

Input = "abaxyzzyxf"
Output = "xyzzyx"
'''

# Solution 1
# Run time complexity: O(n^3), Space complexity: O(n)


def longest_palindromic_substring_1(string):
    count = 1
    start = 0
    for i in range(len(string)):
        right = len(string)-1
        while right > i:
            if isPalindrome(string, i, right):
                new_count = right - i + 1
                if new_count > count:
                    start = i
                    count = new_count

                break

            right -= 1

    return string[start:start+count]


def isPalindrome(string, left, right):
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True

# Solution 2
# Run time complexity: O(n^2), Space complexity: O(n)
# Start from the beginning. Consider each item as the center of prospective palindrome (odd no length)
# Also consider the empty string before current item as center of prospective palindrome (even no length)


def longest_palindromic_substring_2(string):
    result = [0, 0]
    for i in range(1, len(string)):
        # Consider i as the center of the prospective palindrome
        odd_result = check_palindrome(string, i-1, i+1)

        # Consider empty string before i as the center of the prospective palindrome
        even_result = check_palindrome(string, i-1, i)

        # Take the max of both
        max_result = max(odd_result, even_result, key=lambda x: x[1]-x[0])

        # Update result
        result = max(result, max_result, key=lambda x: x[1] - x[0])

    return string[result[0]: result[1]+1]


def check_palindrome(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1

    # Single character is always plaindrome
    return [left+1, right-1] if left < right else [left, left]


if __name__ == "__main__":
    print(longest_palindromic_substring_1("abaxyzzyxf"))
    print(longest_palindromic_substring_2("abaxyzzyxf"))
