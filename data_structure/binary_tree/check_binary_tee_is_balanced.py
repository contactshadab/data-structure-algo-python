from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    def is_balanced(self):
        return self.__is_balanced(self.root)

    def __is_balanced(self, root):
        if root is None:
            return True

        if abs(self.__get_balance_factor(root)) > 1:
            return False

        return self.__is_balanced(root.left_child) and self.__is_balanced(root.right_child)

    def __get_balance_factor(self, root):
        return self.__height(root.left_child) - self.__height(root.right_child)

    def __height(self, root):
        if root is None:
            return -1

        return 1 + max(self.__height(root.left_child), self.__height(root.right_child))


if __name__ == "__main__":
    # Populate binary search tree 1
    binary_tree = MyBinaryTree()

    print(binary_tree.is_balanced())    # True, Empty tree is balanced

    binary_tree.insert(10)
    print(binary_tree.is_balanced())    # True

    binary_tree.insert(30)
    print(binary_tree.is_balanced())    # True

    binary_tree.insert(20)
    print(binary_tree.is_balanced())    # False

    binary_tree.insert(60)
    binary_tree.insert(50)

    print(binary_tree.is_balanced())    # False
