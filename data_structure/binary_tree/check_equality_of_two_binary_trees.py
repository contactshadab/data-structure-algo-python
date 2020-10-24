from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    # Check equality of two binary trees
    def equals(self, another_tree):
        return self.__equals(self.root, another_tree.root)

    def __equals(self, node1, node2):
        # If both node are None we need to return from recursion for this path
        if node1 is None and node2 is None:
            return True

        # If only one of the both node is None return False
        if node1 is None or node2 is None:
            return False

        # If any unequality is found we do not need to continue
        if node1.value != node2.value:
            return False

        # Check both childs for quality
        return self.__equals(node1.left_child, node2.left_child) and self.__equals(node1.right_child, node2.right_child)


if __name__ == "__main__":
    # Populate binary search tree 1
    binary_tree = MyBinaryTree()
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)

    # Populate binary search tree 2
    binary_tree2 = BinaryTree()
    binary_tree2.insert(10)
    binary_tree2.insert(30)
    binary_tree2.insert(20)
    binary_tree2.insert(60)
    # binary_tree2.insert(50)   # Uncommenting this will make both trees equal

    # Check equality of two trees
    print(binary_tree.equals(binary_tree2))  # False
