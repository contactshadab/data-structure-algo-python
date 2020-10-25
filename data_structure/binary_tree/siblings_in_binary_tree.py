from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):
    def are_siblings(self, value1, value2):
        if self.root is None:
            raise Exception('Empty tree')

        if None in [value1, value2]:
            raise Exception('Illegal arguments')

        return self.__are_siblings(self.root, sorted([value1, value2]))

    def __are_siblings(self, root, values):
        if root is None:
            return False

        if root.left_child is not None and root.right_child is not None and sorted([root.left_child.value, root.right_child.value]) == values:
            return True

        return self.__are_siblings(root.left_child, values) or self.__are_siblings(root.right_child, values)


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
    print(binary_tree.are_siblings(5, 30))  # True
    print(binary_tree.are_siblings(30, 5))  # True
    print(binary_tree.are_siblings(50, 60))   # False
    print(binary_tree.are_siblings(20, 20))  # False
    print(binary_tree.are_siblings(20, 60))  # True
    print(binary_tree.are_siblings(6, 20))  # False
    print(binary_tree.are_siblings(6, 4))  # True
