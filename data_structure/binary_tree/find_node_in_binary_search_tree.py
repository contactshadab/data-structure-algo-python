from binary_search_tree_implementation import BinaryTree


class MyBinarySeachTree(BinaryTree):

    # Find in a Binary Search Tree
    def find(self, value):
        if self.root is None:
            raise Exception('Empty tree')

        current = self.root
        while current is not None:
            if value == current.value:
                return True

            if (value < current.value):
                current = current.left_child
            else:
                current = current.right_child

        return False

    # Find in a Binary Search Tree with recursion
    def find_with_recursion(self, value):
        if self.root is None:
            raise Exception('Empty tree')

        return self.__find(self.root, value)

    def __find(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self.__find(node.left_child, value)
        else:
            return self.__find(node.right_child, value)


if __name__ == "__main__":
    # Populate binary search tree
    binary_search_tree = MyBinarySeachTree()
    binary_search_tree.insert(10)
    binary_search_tree.insert(30)
    binary_search_tree.insert(20)
    binary_search_tree.insert(60)

    # Find
    print(30, binary_search_tree.find(30))
    print(-100, binary_search_tree.find(-100))
