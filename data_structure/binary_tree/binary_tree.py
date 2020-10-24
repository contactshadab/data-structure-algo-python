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

    # Height of Binary Tree is the maximum no of edges from its leaf to its root
    # Algo: height of a sub tree is 1 + height of its subtree till we encounter None
    def height(self):
        return self.__height(self.root)

    # Depth of a Binary Search Tree node is the no of edges from its root to the node
    # Algo: Keep finding the node in right left/right subtree and keep count of edges
    def depth(self, value):
        current = self.root
        edges = 0
        while current is not None:
            if current.value == value:
                break

            if value < current.value:
                current = current.left_child
            else:
                current = current.right_child

            edges += 1

        return edges if current else -1

    # Although the insert() function inserts into binary searech tree.
    # For this implementation assume we have Binary Tree, not Binary Search Tree.
    def min_in_binary_tree(self):
        return self.__min_in_binary_tree(self.root)

    # Check equality of two binary trees
    def equals(self, another_tree):
        return self.__equals(self.root, another_tree.root)

    # Validate Binary Search Tree
    def validate(self):
        return self.__validate(self.root, -float('inf'), float('inf'))

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

    def __find(self, node, value):
        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self.__find(node.left_child, value)
        else:
            return self.__find(node.right_child, value)

    def __height(self, node):
        if node is None:
            return -1

        return 1 + max(self.__height(node.left_child), self.__height(node.right_child))

    def __min_in_binary_tree(self, node):
        # If we reach a child of leaf return None because that node does not exist
        if node is None:
            return None

        # Get min of left and right subtrees
        min_left = self.__min_in_binary_tree(node.left_child)
        min_right = self.__min_in_binary_tree(node.right_child)

        # If it is a leaf, this is the min for this subtree
        if min_left is None and min_right is None:
            return node.value

        # If one of the child is not present either the node or the other node will be min
        if min_left is None or min_right is None:
            return min(min_left, node.value) if min_right is None else min(min_right, node.value)

        # If both childs are present, calculate min between node and both child nodes
        return min(min_left, min_right, node.value)

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

    def __validate(self, node, min, max):
        if node is None:
            return True

        if node.value < min or node.value > max:
            return False

        return self.__validate(node.left_child, -float('inf'), node.value-1) and self.__validate(node.right_child, node.value+1, float('inf'))


# Tests
if __name__ == "__main__":
    binary_tree = BinaryTree()
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)
    binary_tree.pre_order_traverse()
    print("---")
    binary_tree.in_order_traverse()
    print("---")
    binary_tree.post_order_traverse()
    print(30, binary_tree.find(30))
    print(-100, binary_tree.find(-100))
    print(binary_tree.height())
    print(binary_tree.depth(50))
    print(binary_tree.min_in_binary_tree())

    # Check equality of two trees
    binary_tree2 = BinaryTree()
    binary_tree2.insert(10)
    binary_tree2.insert(30)
    binary_tree2.insert(20)
    binary_tree2.insert(60)
    # binary_tree2.insert(50)   # Uncommenting this will make both trees equal
    print(binary_tree.equals(binary_tree2))  # False

    # Validate binary search tree
    print(binary_tree.validate())
