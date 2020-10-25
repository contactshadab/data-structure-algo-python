from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    def count_leaves(self):
        return self.__count_leaves(self.root)

    def __count_leaves(self, root):
        if root is None:
            return 0

        if root.left_child is None and root.right_child is None:
            return 1

        return self.__count_leaves(root.left_child) + self.__count_leaves(root.right_child)


if __name__ == "__main__":
    binary_tree = MyBinaryTree()

    # Populate binary search tree
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)
    binary_tree.insert(5)
    binary_tree.insert(4)
    binary_tree.insert(6)

    print(binary_tree.count_leaves())
