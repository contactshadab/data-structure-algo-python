'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lower-case English letters.

'''


# Solution 1
# Run time complexity: O(M * Nlog N), where M is no of words and N is the max no of characters in word
# Space complexity: O(M * N)
def group_anagrams(strs):
    anagrams = {}

    for anagram in strs:
        sorted_str = tuple(sorted(anagram))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(anagram)
        else:
            anagrams[sorted_str] = [anagram]

    return anagrams.values()


# Solution 2
# Run time complexity: O(M * N), where M is no of words and N is the max no of characters in word
# Space complexity: O(M * N)
def group_anagrams_2(strs):
    anagrams = {}

    for word in strs:
        counts = [0 for i in range(26)]
        j = 0
        while j < len(word):
            counts[ord(word[j]) - ord('a')] += 1
            j += 1

        if tuple(counts) in anagrams:
            anagrams[tuple(counts)].append(word)
        else:
            anagrams[tuple(counts)] = [word]

    return anagrams.values()


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    print(group_anagrams_2(["eat", "tea", "tan", "ate", "nat", "bat"]))
