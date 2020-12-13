'''
https://leetcode.com/problems/reorder-list/
143. Reorder List

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''


def get_mid(self, head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next if fast.next else None

    return slow


def reorderList(self, head: ListNode) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    if head is None:
        return None

    # Get mid
    mid = self.get_mid(head)

    # Reverse the second half of the list (1 -> 2 -> 3 & 6 -> 5 -> 4 )
    p = mid
    prev = None
    while p is not None:
        next = p.next
        p.next = prev

        prev = p
        p = next

    # Merge both lists (1 -> 6 -> 2 -> 5 -> 3 -> 4)
    p1, p2 = head, prev
    while p2.next:
        p1_next = p1.next
        p2_next = p2.next

        p2.next = p1.next
        p1.next = p2

        p1 = p1_next
        p2 = p2_next
