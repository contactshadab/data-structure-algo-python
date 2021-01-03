'''
https://leetcode.com/problems/word-break/
139. Word Break
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

'''


# Solution 1: Recursion and backtracking
# Run time complexity: O(n^3), n for recusrion depth, for each recursive call we have upto n iterations of for loop. And substring cost n
# Space complexity: O(n), depth of the recursion tree
def word_break(s, wordDict):

    def backtrack(start):
        if start == len(s):
            return True

        if start in memoise:
            return memoise[start]

        for end in range(start+1, len(s)+1):
            first = s[start: end] in words
            if first and backtrack(end):
                memoise[start] = True
                return True

        memoise[start] = False
        return False

    words = set(wordDict)
    memoise = {}
    return backtrack(0)


# Solution 1: Recursion and backtracking
# Run time complexity: O(n^3)
# Space complexity: O(n), for storing n+1 length dp array
def word_break_2(s, wordDict):
    words = set(wordDict)
    dp = [False for i in range(len(s)+1)]
    dp[0] = True
    for end in range(1, len(s)+1):
        for start in range(end):
            if dp[start] and s[start: end] in words:
                dp[end] = True
                break

    return dp[-1]


if __name__ == "__main__":
    print(word_break("leetcode", ["leet", "code"]))
