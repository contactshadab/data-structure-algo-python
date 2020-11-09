# Run time complexity: O(n), Space complexity: O(n)
def balanced_brackets(string):
    stack = []
    brackets = {")": "(", "}": "{", "]": "["}
    opening_brackets = brackets.values()
    closing_brackets = brackets.keys()
    for ch in string:
        if ch in closing_brackets:
            if len(stack) == 0 or stack[-1] != brackets[ch]:
                return False
            stack.pop()
        elif ch in opening_brackets:
            stack.append(ch)

    return len(stack) == 0


if __name__ == "__main__":
    print(balanced_brackets("([])(){}(())()()"))
