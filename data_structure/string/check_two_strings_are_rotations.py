'''
Problem:
Check if a string is a rotation of another string.
Input: “ABCD”, “DABC” (rotate one char to the right)
Output: true 
Input: “ABCD”, “CDAB” (rotate two chars to the right)
Output: true
Input: “ABCD”, “ADBC”
Output: false

Intuition:
Even when the string is rotated the order of characters does not change.
“ABCD”, “DABC”
In this example B is always after A, C after B and D after C.
The only difference is the character may be present at the first index if teh previous one is at last index
If we append “ABCD” with itself it becomes “ABCDABCD”. This string will have all rotations of "ABCD"

'''


def is_rotations(first, second):
    if first is None or second is None:
        raise Exception('Illegal argument')

    return len(first) == len(second) and second in first + first


if __name__ == "__main__":
    print(is_rotations("ABCD", "CDAB"))  # True
    print(is_rotations("AB", "BA"))  # True
    print(is_rotations("ABCD", "ABCD"))  # True
    print(is_rotations("ABCD", "CDA"))  # False
    # print(is_rotations("ABCD", None))    # Exception: Illegal argument
