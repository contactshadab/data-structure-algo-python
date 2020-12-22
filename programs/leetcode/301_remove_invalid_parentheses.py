'''
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]

'''


class Solution:

    def __init__(self):
        self.result = set()
        self.min = float('inf')

    # Time Complexity: O(2^n), in wirst case if we have all opening brackets we have 2 choices for every character
    # Space Complexity: O(n), for recursive call stack
    def remove_invalid_parentheses(self, s):

        def backtrack(expr, i, left, right, removed_count):
            if i == len(s):
                if left == right and removed_count <= self.min:
                    if removed_count < self.min:
                        self.min = removed_count
                        self.result = set()
                    self.result.add(''.join(expr))

                return

            if s[i] not in '()':
                expr.append(s[i])
                backtrack(expr, i+1, left, right, removed_count)
                expr.pop()
            else:
                backtrack(expr, i+1, left, right, removed_count+1)

                expr.append(s[i])
                if s[i] == '(':
                    backtrack(expr, i+1, left+1, right, removed_count)
                # We go into recursion only if we have more opening brackets than closing brackets
                elif right < left:
                    backtrack(expr, i+1, left, right+1, removed_count)

                expr.pop()

        backtrack([], 0, 0, 0, 0)
        return list(self.result)


sol = Solution()
print(sol.remove_invalid_parentheses("()())()"))


# This is more optimum solution as in previous solution we first made the expression and then we checked if it is valid or not
# In this approach we know beforehand how many left and right paranthesis are at invalid position and we do not exclude more than that
class Solution2:

    def __init__(self):
        self.result = set()
        self.min = float('inf')

    # Although in average case it is an optimum solution that the previous one in worst case it has same time complexity
    # Time Complexity: O(2^n), in wirst case if we have all opening brackets we have 2 choices for every character
    # Space Complexity: O(n), for recursive call stack
    def removeInvalidParentheses(self, s):

        def backtrack(expr, i, left, right, left_misplaced_count, right_misplaced_count):
            if i == len(s):
                if left_misplaced_count == 0 and right_misplaced_count == 0:
                    self.result.add(''.join(expr))

                return

            if s[i] not in '()':
                # Include the character
                expr.append(s[i])
                backtrack(expr, i+1, left, right,
                          left_misplaced_count, right_misplaced_count)
                expr.pop()
            else:
                # Exclude the paranthesis as long as we have not exhausted required exclusions
                if s[i] == '(' and left_misplaced_count > 0:
                    backtrack(expr, i+1, left, right,
                              left_misplaced_count - 1, right_misplaced_count)
                elif s[i] == ')' and right_misplaced_count > 0:
                    backtrack(expr, i+1, left, right,
                              left_misplaced_count, right_misplaced_count - 1)

                # Include the paranthesis
                expr.append(s[i])

                if s[i] == '(':
                    backtrack(expr, i+1, left+1, right,
                              left_misplaced_count, right_misplaced_count)
                elif right < left:
                    backtrack(expr, i+1, left, right+1,
                              left_misplaced_count, right_misplaced_count)

                expr.pop()

        def misplaced_paranthesis(s):
            left, right = 0, 0
            for ch in s:
                if ch == '(':
                    left += 1
                elif ch == ')':
                    if left > 0:
                        left -= 1
                    else:
                        right += 1

            return left, right

        left_misplaced_count, right_misplaced_count = misplaced_paranthesis(s)
        backtrack([], 0, 0, 0, left_misplaced_count, right_misplaced_count)
        return list(self.result)
