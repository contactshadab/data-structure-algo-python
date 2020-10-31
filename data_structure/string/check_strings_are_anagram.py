'''
Detect if two strings are anagram of each other. A string is an
anagram of another string if it has the exact same characters in any
order.
Input: “abcd”, “adbc”
Output: true
Input: “abcd”, “cadb”
Input: true
Input: “abcd”, “abcd”
Output: true
Input: “abcd”, “abce”
Output: false
'''


def are_anagram(first, second):
    if first is None or second is None or len(first) != len(second):
        return False

    return sorted(first) == sorted(second)


# Assume we have only English characters
def are_anagram_histogramming_approach(first, second):
    if first is None or second is None or len(first) != len(second):
        return False

    _ENGLISG_ALPHABETS_COUNT = 26
    frequencies = [0] * _ENGLISG_ALPHABETS_COUNT

    for ch in first.lower():
        frequencies[ord(ch) - ord('a')] += 1

    for ch in second.lower():
        index = ord(ch) - ord('a')    # Get index from 0 to 25
        # If frequency at this index is already 0 it means both lists do not have equal count of that character
        if frequencies[index] == 0:
            return False

        frequencies[index] -= 1

    return True


if __name__ == "__main__":
    print(are_anagram("abcd!", "a!bdc"))  # True
    print(are_anagram("abcd", "abde"))  # False
    print(are_anagram("abcd", "abdcc"))  # False
    print(are_anagram("abcd", None))  # False
    print(are_anagram("", ""))  # True
    print(are_anagram("a", "a"))  # True

    print(are_anagram_histogramming_approach("abcdd", "aBdc"))  # True
    print(are_anagram_histogramming_approach("aa", "ad"))  # False
