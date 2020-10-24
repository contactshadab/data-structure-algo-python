# This module has the implementation of Binary Tree
# Some implementations like insert, find, depth assume it is a Binary Search Tree
# While some other implementations like traversals, min, height assume it is Binary Tree

class Node:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None


class BinaryTree:

    def __init__(self):
        self.root = None

    # Insert in a Binary Search Tree
    def insert(self, value):
        self.root = self.__insert(self.root, value)

    # Binary Tree Pre order traversal
    def pre_order_traverse(self):
        self.__pre_order_traverse(self.root)

    # Binary Tree In order traversal
    def in_order_traverse(self):
        self.__in_order_traverse(self.root)

    # Binary Tree Post order traversal
    def post_order_traverse(self):
        self.__post_order_traverse(self.root)

    def height(self):
        return self.__height(self.root)

    # ----------------------------------------------------------------------------
    #                   All private methods from here
    # ----------------------------------------------------------------------------

    def __insert(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left_child = self.__insert(node.left_child, value)
        else:
            node.right_child = self.__insert(node.right_child, value)

        return node

    def __pre_order_traverse(self, node):
        if node is None:
            return

        print(node.value)
        self.__pre_order_traverse(node.left_child)
        self.__pre_order_traverse(node.right_child)

    def __in_order_traverse(self, node):
        if node is None:
            return

        self.__in_order_traverse(node.left_child)
        print(node.value)
        self.__in_order_traverse(node.right_child)

    def __post_order_traverse(self, node):
        if node is None:
            return

        self.__post_order_traverse(node.left_child)
        self.__post_order_traverse(node.right_child)
        print(node.value)

    def __height(self, node):
        if node is None:
            return -1

        return 1 + max(self.__height(node.left_child), self.__height(node.right_child))


# Tests
if __name__ == "__main__":
    # Instantiate binary search tree
    binary_tree = BinaryTree()

    # Populate binary search tree
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)

    # Traversal
    binary_tree.pre_order_traverse()
    print("---")
    binary_tree.in_order_traverse()
    print("---")
    binary_tree.post_order_traverse()
