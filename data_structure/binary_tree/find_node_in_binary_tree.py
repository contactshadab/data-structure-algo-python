from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):
    def find(self, value):
        return self.__find(self.root, value)

    def __find(self, root, value):
        if root is None:
            return False

        if root.value == value:
            return True

        return self.__find(root.left_child, value) or self.__find(root.right_child, value)


if __name__ == "__main__":
    binary_tree = MyBinaryTree()

    # Populate binary tree
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)
    binary_tree.insert(5)
    binary_tree.insert(4)
    binary_tree.insert(6)

    # Find
    print(binary_tree.find(10))  # True
    print(binary_tree.find(-100))   # False
    print(binary_tree.find(50))  # True
    print(binary_tree.find(60))  # True
