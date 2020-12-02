'''
https://leetcode.com/problems/minimum-window-substring/
76. Minimum Window Substring
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Example 2:

Input: s = "a", t = "a"
Output: "a"
 

Constraints:

1 <= s.length, t.length <= 105
s and t consist of English letters.
'''


def min_window(s, t):

    t_count = {}
    for ch in t:
        t_count[ch] = t_count.get(ch, 0) + 1

    res = [float('inf'), None, None]
    c_count = {}

    left, right = 0, 0
    matched = 0
    while right < len(s):
        ch = s[right]
        c_count[ch] = c_count.get(ch, 0) + 1
        if ch in t_count and c_count[ch] == t_count[ch]:
            matched += 1

        # If we find all matches
        # We found the right window now collapse it and check if it is still right
        while left <= right and matched == len(t_count):
            if right - left + 1 < res[0]:
                res = [right - left + 1, left, right]

            left_ch = s[left]
            c_count[left_ch] -= 1
            if left_ch in t_count and c_count[left_ch] < t_count[left_ch]:
                matched -= 1

            left += 1

        right += 1

    return s[int(res[1]): int(res[2])+1] if res[0] != float('inf') else ""


if __name__ == "__main__":
    print(min_window("ADOBECODEBANC", "ABC"))
