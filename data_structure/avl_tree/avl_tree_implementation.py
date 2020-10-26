class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVLTree:

    def __init__(self):
        self.root = None

    # Insert in a Binary Search Tree
    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left_child = self.__insert(root.left_child, value)
        else:
            root.right_child = self.__insert(root.right_child, value)

        # If we have reached here, we just added a new child node
        # Increase height of root node by 1 of max height of child node.
        root.height = 1 + max(self.__get_height(root.left_child),
                              self.__get_height(root.right_child))

        # Balance teh tree if the subtree is unbalanced and get new root
        root = self.__balance(root)

        return root

    def __get_height(self, root):
        return root.height if root else -1

    def __get_balance_factor(self, root):
        return self.__get_height(root.left_child) - self.__get_height(root.right_child)

    def __is_left_heavy(self, root):
        return self.__get_balance_factor(root) > 1

    def __is_right_heavy(self, root):
        return self.__get_balance_factor(root) < -1

    def __balance(self, root):
        if self.__is_left_heavy(root):
            if self.__get_balance_factor(root.left_child) < 0:
                # Tree is Left-right heavy
                # Need to do Left-right rotation. First do left rotation on its left child
                root.left_child = self.__rotate_left(root.left_child)

            root = self.__rotate_right(root)
        elif self.__is_right_heavy(root):
            if self.__get_balance_factor(root.right_child) > 0:
                # Tree is Right-left heavy
                # Need to do Right-left rotation. First do right rotation on its right child
                root.right_child = self.__rotate_right(root.right_child)

            root = self.__rotate_left(root)

        return root

    def __rotate_left(self, root):
        # Perform left rotation
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root

        # Recalculate height of old and new root
        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __rotate_right(self, root):
        # Perform right rotation
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root

        # Recalculate height of old and new root
        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __set_height(self, node):
        node.height = 1 + max(self.__get_height(node.left_child),
                              self.__get_height(node.right_child))


# Tests
if __name__ == "__main__":
    # Instantiate AVL Tree
    avl_tree = AVLTree()

    # Populate tree
    avl_tree.insert(10)
    avl_tree.insert(20)
    avl_tree.insert(15)
    avl_tree.insert(30)
