class Heapify:

    def __init__(self, items):
        self.items = items

    def heapify(self):
        # Instead of iterating through all nodes we can save some time by not checking leaf nodes
        # since they are already following Heap Conditions
        # Also if we go bottom to up we can save some recursive calls as the subtree will already be following Heap Conditions
        last_parent_index = (int)(len(self.items)/2 - 1)
        for i in range(last_parent_index, -1):
            self._heapify(i)

    def _heapify(self, index):
        while index < len(self.items) and not self._is_valid_parent(index):
            # The direction to bubble down node that is greator than its child
            max_child_index = index
            if self._has_left(index) and self._left_item(index) > self.items[index]:
                max_child_index = self._left_index(index)
            if self._has_right(index) and self._right_item(index) > self.items[index]:
                max_child_index = self._right_index(index)

            # If parent is already larger, dont do anything
            if index == max_child_index:
                return

            # Swap parent-child nodes
            self._swap(index, max_child_index)

            # Keep bubbling down
            index = max_child_index

    def _is_valid_parent(self, index):
        # If it does not have a left child it is a leaf since in heap we fill from left to right
        if not self._has_left(index):
            return True

        if not self._has_right(index):
            return self.items[index] >= self._left_item(index)

        return self.items[index] >= self._left_item(index) and self.items[index] >= self._right_item(index)

    def _swap(self, parent, child):
        temp = self.items[parent]
        self.items[parent] = self.items[child]
        self.items[child] = temp

    def _max_child_index(self, index):
        if not self._has_right(index):
            return self._left_index(index)

        if self._left_item(index) > self._right_item(index):
            return self._left_index(index)
        else:
            self._right_index(index)

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


if __name__ == "__main__":
    items = [5, 3, 8, 4, 1, 2]
    heapify = Heapify(items)
    heapify.heapify()
    print(items)
