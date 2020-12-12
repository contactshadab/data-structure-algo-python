'''
https://leetcode.com/problems/copy-list-with-random-pointer/
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.

'''


# Solution 1
# Run time complexity: O(n)
# Space complexity: O(n)
def copy_random_list(head):
    p1 = head
    copy = p2 = Node(0)
    visited = {}
    while p1 is not None:
        # If p1 does not exist in visited, create it
        if p1 in visited:
            p2.next = visited[p1]
        else:
            node = Node(p1.val)
            p2.next = node
            visited[p1] = node

        # If random does not exist in visited, create it
        if p1.random:
            if p1.random in visited:
                p2.next.random = visited[p1.random]
            else:
                node = Node(p1.random.val)
                p2.next.random = node
                visited[p1.random] = node
        else:
            p2.next.random = None

        p2 = p2.next
        p1 = p1.next

    return copy.next


# Solution 2 - Interweave both lists (A -> Copy A -> B -> Copy B)
# Run time complexity: O(n)
# Space complexity: O(1)
def copy_random_list_2(self, head: 'Node') -> 'Node':
    if not head:
        return None

    p1 = head
    while p1 is not None:
        node = Node(p1.val)

        node.next = p1.next
        p1.next = node

        p1 = node.next

    p1 = head
    while p1:
        p1.next.random = p1.random.next if p1.random else None

        p1 = p1.next.next

    p1, p2, copy = head, head.next, head.next
    while p1:
        print(p1.val)
        p1.next = p1.next.next
        p2.next = p2.next.next if p2.next else None

        p1 = p1.next
        p2 = p2.next

    return copy
