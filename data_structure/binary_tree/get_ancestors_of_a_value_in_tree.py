from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    def get_ancestors(self, value):
        nodes = []
        self.__get_ancestors(self.root, value, nodes)

        return nodes

    def __get_ancestors(self, root, value, nodes):
        if root is None:
            return False

        # If found the node just return from here. We need its ansestors, not this node
        if root.value == value:
            return True

        if self.__get_ancestors(root.left_child, value, nodes) or self.__get_ancestors(root.right_child, value, nodes):
            nodes.append(root.value)
            return True

        return False


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

    print(binary_tree.get_ancestors(10))    # Empty list since it is root
    print(binary_tree.get_ancestors(60))    # [30, 10]
    print(binary_tree.get_ancestors(50))    # [60, 30, 10]
    print(binary_tree.get_ancestors(6))    # [5, 10]
