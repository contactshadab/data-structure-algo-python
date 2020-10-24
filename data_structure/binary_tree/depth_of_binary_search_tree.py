from binary_search_tree_implementation import BinaryTree


class MyBinarySeachTree(BinaryTree):

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


if __name__ == "__main__":

    # Populate binary search tree
    binary_search_tree = MyBinarySeachTree()
    binary_search_tree.insert(10)
    binary_search_tree.insert(30)
    binary_search_tree.insert(20)
    binary_search_tree.insert(50)
    binary_search_tree.insert(60)

    print(binary_search_tree.depth(50))
