# Max Heap implementation
class Heap:

    def __init__(self):
        self.items = []

    def insert(self, item):
        self.items.append(item)

        # Bubble up if heap condition fails
        self._bubble_up()

    def _bubble_up(self):
        index = len(self.items) - 1

        while index > 0 and self.items[index] > self._parent_item(index):
            # Swap child-parent values
            self._swap(index, self._parent_index(index))

            # Go up towards the root
            index = self._parent_index(index)

    def _parent_index(self, index):
        return (int)((index - 1) / 2)

    def _parent_item(self, index):
        return self.items[self._parent_index(index)]

    def _swap(self, parent, child):
        temp = self.items[parent]
        self.items[parent] = self.items[child]
        self.items[child] = temp

    def remove(self):
        if len(self.items) == 0:
            raise Exception('Empty Heap')

        # Remove the root, i.e first item in list and replace it with the last item in the list (last left in heap)
        removed = self.items[0]
        self.items[0] = self.items.pop()

        # Bubble down if heap condition fails
        self._bubble_down()

        return removed

    def _bubble_down(self):
        index = 0
        while index < len(self.items)-1 and not self._is_valid_parent(index):
            # The larger value of the two childs is the direction to bubble down
            max_child_index = self._max_child_index(index)

            # Swap parent-child values
            self._swap(index, max_child_index)

            # Our route to bubble down is the child with max value
            index = max_child_index

    def _is_valid_parent(self, index):
        # If it does not have a left child it is a leaf since in heap we fill from left to right
        if not self._has_left(index):
            return True

        if not self._has_right(index):
            return self.items[index] >= self._left_item(index)

        return self.items[index] >= self._left_item(index) and self.items[index] >= self._right_item(index)

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


# Tests
if __name__ == "__main__":
    # Instantiate
    heap = Heap()

    # Populate data
    heap.insert(30)
    heap.insert(20)
    heap.insert(10)
    heap.insert(40)
    heap.insert(15)

    print(heap.items)

    # Remove the root
    print(heap.remove())
    print(heap.items)
