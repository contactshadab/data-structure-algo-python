'''
https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display(self):
        p = self
        while p is not None:
            print(p.val, end=" ")

            p = p.next


# Run time complexity: O(N) where N is the max number of items in between lists
# Space complexity: O(1)
def sum_list(l1, l2):
    head = ListNode()
    p1, p2, p = l1, l2, head

    carry = 0
    while p1 is not None or p2 is not None:
        first = p1.val if p1 is not None else 0
        second = p2.val if p2 is not None else 0
        sum = first + second + carry
        carry = sum // 10
        sum = sum % 10
        p.next = ListNode(sum, None)

        p = p.next
        p1 = p1.next if p1 is not None else None
        p2 = p2.next if p2 is not None else None

    if carry:
        p.next = ListNode(carry, None)

    return head.next


if __name__ == "__main__":
    l1 = NodeList(9, NodeList(0, NodeList(8, None)))
    l2 = NodeList(8, NodeList(2, NodeList(9, None)))

    sum = sum_list(l1, l2)
    sum.display()
