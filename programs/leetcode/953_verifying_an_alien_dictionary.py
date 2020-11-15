'''
https://leetcode.com/problems/verifying-an-alien-dictionary
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
'''


def is_alien_sorted(words, order):
    dict = {ch: index for index, ch in enumerate(order)}

    for i in range(1, len(words)):
        previous_word = words[i-1]
        current_word = words[i]

        # Find the first difference or end of one of the words
        j = 0
        while j < len(current_word) and j < len(previous_word) and current_word[j] == previous_word[j]:
            j += 1

        # If the second word is shorter than first word they are not sorted correctly
        if j < len(previous_word) and j >= len(current_word):
            return False

        # Check the order
        if j < len(current_word) and j < len(previous_word) and dict[current_word[j]] < dict[previous_word[j]]:
            return False

    return True


if __name__ == "__main__":
    print(is_alien_sorted(["hello", "leetcode"],
                          "hlabcdefgijkmnopqrstuvwxyz"))    # True
    print(is_alien_sorted(["word", "world", "row"],
                          "worldabcefghijkmnpqstuvxyz"))    # False
