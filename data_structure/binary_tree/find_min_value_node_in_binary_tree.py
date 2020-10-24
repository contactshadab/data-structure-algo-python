from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    # Although the insert() function in BinaryTree inserts into binary searech tree.
    # For this implementation assume we have Binary Tree, not Binary Search Tree.
    def min_in_binary_tree(self):
        return self.__min_in_binary_tree(self.root)

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


if __name__ == "__main__":
    # Populate binary search tree
    binary_tree = MyBinarySeachTree()
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)

    print(binary_tree.min_in_binary_tree())
