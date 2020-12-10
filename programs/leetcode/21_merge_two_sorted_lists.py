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
        print("")


# Solution 1
# Run time complexity: O(M+N) where M and N are the number of items in both lists
# Space complexity: O(1)
def merge_two_lists(l1, l2):
    head = ListNode()
    prev = head
    while l1 is not None or l2 is not None:
        if l2 is None or (l1 is not None and l1.val < l2.val):
            prev.next = l1
            prev = l1
            l1 = l1.next
        else:
            prev.next = l2
            prev = l2
            l2 = l2.next

    return head.next


# Solution 2:
# Run time complexity: O(M+N) where M and N are the number of items in both lists
# Space complexity: O(M+N)
def merge_two_lists_recursion(l1, l2):
    if not l1:
        return l2

    if not l2:
        return l1

    if l1.val < l2.val:
        l1.next = merge_two_lists_recursion(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_lists_recursion(l1, l2.next)
        return l2


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(2, ListNode(4, None)))
    l2 = ListNode(1, ListNode(5, ListNode(7, None)))

    res = merge_two_lists(l1, l2)
    res.display()

    res = merge_two_lists_recursion(l1, l2)
    res.display()
