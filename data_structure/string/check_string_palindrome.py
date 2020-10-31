
def is_palindrome(str):
    if str is None:
        raise Exception('Illegal argument')

    left = 0
    right = len(str)-1

    while left < right:
        if str[left] != str[right]:
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    print(is_palindrome("abba"))  # True
    print(is_palindrome("abcba"))  # True
    print(is_palindrome(""))  # True
    print(is_palindrome("abca"))  # False
