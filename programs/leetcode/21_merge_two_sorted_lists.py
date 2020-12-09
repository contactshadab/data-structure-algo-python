'''
https://leetcode.com/problems/merge-two-sorted-lists/
21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: l1 = [], l2 = []
Output: []

Example 3:
Input: l1 = [], l2 = [0]
Output: [0]

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.
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
# Space complexity: O(N)
def merge_two_lists(l1, l2):
    head = ListNode()
    p1, p2, p = l1, l2, head

    while p1 is not None and p2 is not None:
        if p1.val < p2.val:
            p.next = ListNode(p1.val)
            p1 = p1.next
        else:
            p.next = ListNode(p2.val)
            p2 = p2.next

        p = p.next

    p1 = p2 if p1 is None else p1
    while p1 is not None:
        p.next = ListNode(p1.val)

        p = p.next
        p1 = p1.next

    return head.next


if __name__ == "__main__":
    l1 = ListNode(1, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(3, ListNode(4, None)))
    res = merge_two_lists(l1, l2)
    res.display()
