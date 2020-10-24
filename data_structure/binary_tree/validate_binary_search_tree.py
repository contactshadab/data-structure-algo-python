from binary_search_tree_implementation import BinaryTree


class MyBinarySeachTree(BinaryTree):

    # Validate Binary Search Tree
    def validate(self):
        return self.__validate(self.root, -float('inf'), float('inf'))

    def __validate(self, node, min, max):
        if node is None:
            return True

        if node.value < min or node.value > max:
            return False

        return self.__validate(node.left_child, -float('inf'), node.value-1) and self.__validate(node.right_child, node.value+1, float('inf'))

    # This method is just used to invalidate the binary search tree so that we can test validate() method
    def swap(self):
        temp = self.root.left_child
        self.root.left_child = self.root.right_child
        self.root.right_child = temp


if __name__ == "__main__":
    # Populate binary search tree
    binary_search_tree = MyBinarySeachTree()
    binary_search_tree.insert(10)
    binary_search_tree.insert(30)
    binary_search_tree.insert(20)
    binary_search_tree.insert(60)

    # Validate binary search tree
    print(binary_search_tree.validate())    # True
    binary_search_tree.swap()
    print(binary_search_tree.validate())    # False
