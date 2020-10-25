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

    def size(self):
        return self.__size(self.root)

    # Binary Tree Pre order traversal
    def pre_order_traverse(self):
        nodes = []
        self.__pre_order_traverse(self.root, nodes)

        return nodes

    # Binary Tree In order traversal
    def in_order_traverse(self):
        nodes = []
        self.__in_order_traverse(self.root, nodes)

        return nodes

    # Binary Tree Post order traversal
    def post_order_traverse(self):
        nodes = []
        self.__post_order_traverse(self.root, nodes)

        return nodes

    # Binary Tree Level order traversal or Bredth First Traversal
    def breadth_first_traverse(self):
        if self.root is None:
            print([])
            return

        for i in range(self.height()+1):
            nodes = []
            self.__get_nodes_at_distance(self.root, i, nodes)
            print(nodes)

    # Height of Binary Tree (this implemntation is for both BST and BT)
    def height(self):
        if self.root is None:
            raise Exception('Tree is empty')

        return self.__height(self.root)

    # Maximum in Binary Search Tree
    def max(self):
        if self.root is None:
            raise Exception('Tree is empty')

        return self.__max(self.root)

    # ----------------------------------------------------------------------------
    #                   All private methods from here
    # ----------------------------------------------------------------------------

    def __insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left_child = self.__insert(root.left_child, value)
        else:
            root.right_child = self.__insert(root.right_child, value)

        return root

    def __pre_order_traverse(self, root, nodes):
        if root is None:
            return

        # Add to list
        nodes.append(root.value)

        self.__pre_order_traverse(root.left_child, nodes)
        self.__pre_order_traverse(root.right_child, nodes)

    def __in_order_traverse(self, root, nodes):
        if root is None:
            return

        self.__in_order_traverse(root.left_child, nodes)

        # Add to list
        nodes.append(root.value)

        self.__in_order_traverse(root.right_child, nodes)

    def __post_order_traverse(self, root, nodes):
        if root is None:
            return

        self.__post_order_traverse(root.left_child, nodes)
        self.__post_order_traverse(root.right_child, nodes)

        # Add to list
        nodes.append(root.value)

    def __get_nodes_at_distance(self, root, distance, nodes):
        if root is None:
            return

        # If we reach the distance
        if distance == 0:
            nodes.append(root.value)

        distance = distance - 1
        self.__get_nodes_at_distance(root.left_child, distance, nodes)
        self.__get_nodes_at_distance(root.right_child, distance, nodes)

    def __height(self, root):
        if root is None:
            return -1

        return 1 + max(self.__height(root.left_child), self.__height(root.right_child))

    def __size(self, root):
        if root is None:
            return 0

        return 1 + self.__size(root.left_child) + self.__size(root.right_child)

    def __max(self, root):
        if root.right_child is None:
            return root.value

        return self.__max(root.right_child)


# Tests
if __name__ == "__main__":
    # Instantiate binary search tree
    binary_search_tree = BinaryTree()

    # Get tree size
    print(binary_search_tree.size())  # 0

    print(binary_search_tree.pre_order_traverse())  # Print empty list
    print(binary_search_tree.in_order_traverse())  # Print empty list
    print(binary_search_tree.post_order_traverse())    # Print empty list
    binary_search_tree.breadth_first_traverse()    # Print empty list

    # Populate binary search tree
    binary_search_tree.insert(10)
    binary_search_tree.insert(30)
    binary_search_tree.insert(20)
    binary_search_tree.insert(60)
    binary_search_tree.insert(50)
    binary_search_tree.insert(5)
    binary_search_tree.insert(4)
    binary_search_tree.insert(6)

    # Get tree size
    print(binary_search_tree.size())  # 8

    # Get tree height
    print(binary_search_tree.height())

    # Depth First Traversals
    print(binary_search_tree.pre_order_traverse())
    print(binary_search_tree.in_order_traverse())
    print(binary_search_tree.post_order_traverse())

    # Bredth First Traversals
    binary_search_tree.breadth_first_traverse()

    # Get max
    print(binary_search_tree.max())
