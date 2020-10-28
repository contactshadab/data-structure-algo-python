'''
Implement a min heap. In this implementation, store the items in an array of nodes.
Each node should have two fields: key (integer) and value (string). Nodes should be heapified based on their keys.
'''


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = vars


class MinHeap:

    def __init__(self):
        self.items = []

    def insert(self, key, value):
        self.items.append(Node(key, value))

        self._bubble_up()

    def _bubble_up(self):
        index = len(self.items) - 1
        while index > 0 and self.items[self._parent_index(index)].key > self.items[index].key:
            parent_index = self._parent_index(index)
            self._swap(index, parent_index)
            index = parent_index

    def _parent_index(self, index):
        return (int)((index - 1) / 2)

    def _swap(self, child, parent):
        temp = self.items[child]
        self.items[child] = self.items[parent]
        self.items[parent] = temp

    def remove(self):
        removed = self.items[0].key
        last_leaf = self.items.pop()
        if self.items:
            self.items[0] = last_leaf

        self._bubble_down()

        return removed

    def _bubble_down(self):
        index = 0
        while index < len(self.items)-1 and not self._is_valid_parent(index):
            # The smaller value of the two childs is the direction to bubble down
            min_child_index = self._min_child_index(index)

            # Swap parent-child values
            self._swap(index, min_child_index)

            # Our route to bubble down is the child with max value
            index = min_child_index

    def _is_valid_parent(self, index):
        # If it does not have a left child it is a leaf since in heap we fill from left to right
        if not self._has_left(index):
            return True

        if not self._has_right(index):
            return self.items[index].key <= self._left_item(index).key

        return self.items[index].key <= self._left_item(index).key and self.items[index].key <= self._right_item(index).key

    def _min_child_index(self, index):
        if not self._has_right(index) or self._left_item(index).key < self._right_item(index).key:
            return self._left_index(index)

        return self._right_index(index)

    def _has_left(self, index):
        return self._left_index(index) < len(self.items)

    def _has_right(self, index):
        return self._right_index(index) < len(self.items)

    def _left_item(self, index):
        return self.items[self._left_index(index)]

    def _left_index(self, parent_index):
        return parent_index * 2 + 1

    def _right_item(self, index):
        return self.items[self._right_index(index)]

    def _right_index(self, parent_index):
        return parent_index * 2 + 2

    def display(self):
        if not self.items:
            raise Exception('Empty heap')

        for node in self.items:
            print(node.key, end=" ")
        print("")


if __name__ == "__main__":
    minheap = MinHeap()
    minheap.insert(5, "Five")
    minheap.insert(3, "Three")
    minheap.insert(8, "Eight")
    minheap.insert(4, "Four")
    minheap.insert(1, "One")
    minheap.insert(2, "Two")
    minheap.display()

    print(minheap.remove())
    minheap.display()

    print(minheap.remove())
    minheap.display()

    print(minheap.remove())
    minheap.display()

    print(minheap.remove())
    minheap.display()

    print(minheap.remove())
    minheap.display()

    print(minheap.remove())
    # minheap.display()   # Empty heap Exception
