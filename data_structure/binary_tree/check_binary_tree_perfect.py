from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    '''
        Intiution:
        For a binary tree to be perfect, the relation between height of tree and its size is as below:
        Height -> Size
        0 -> 1
        1 -> 3
        2 -> 7
        3 -> 15

        Formula: 2^(height+1) - 1

    '''

    def is_perfect(self):
        return self.size() == pow(2, self.height()+1) - 1


if __name__ == "__main__":
    # Populate binary search tree 1
    binary_tree = MyBinaryTree()

    # print(binary_tree.is_perfect())    # Exception, Tree is empty

    binary_tree.insert(10)
    print(binary_tree.is_perfect())    # True

    binary_tree.insert(30)
    print(binary_tree.is_perfect())    # False

    binary_tree.insert(20)
    print(binary_tree.is_perfect())    # False

    binary_tree.insert(40)
    print(binary_tree.is_perfect())    # False

    binary_tree.insert(5)
    binary_tree.insert(4)
    binary_tree.insert(6)
    print(binary_tree.is_perfect())    # True
