from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    # Height of Binary Tree is the maximum no of edges from its leaf to its root
    # Algo: height of a sub tree is 1 + height of its subtree till we encounter None
    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return -1

        return 1 + max(self.__height(node.left_child), self.__height(node.right_child))


if __name__ == "__main__":
    # Populate binary search tree 1
    binary_tree = MyBinaryTree()
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)

    print(binary_tree.height())
