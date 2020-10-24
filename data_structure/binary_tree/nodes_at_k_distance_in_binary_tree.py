from binary_search_tree_implementation import BinaryTree


class MyBinaryTree(BinaryTree):

    def nodes_at_distance(self, distance):
        if distance < 0 or distance > self.height():
            raise Exception('Illegal Argument')

        nodes = []
        self.__nodes_at_distance(self.root, distance, nodes)

        return nodes

    def __nodes_at_distance(self, node, distance, nodes):
        if node is None:
            return

        if distance == 0:
            nodes.append(node.value)
            return

        distance = distance - 1
        self.__nodes_at_distance(node.left_child, distance, nodes)
        self.__nodes_at_distance(node.right_child, distance, nodes)


if __name__ == "__main__":
    # Populate binary tree
    binary_tree = MyBinaryTree()
    binary_tree.insert(10)
    binary_tree.insert(30)
    binary_tree.insert(20)
    binary_tree.insert(60)
    binary_tree.insert(50)

    print(binary_tree.nodes_at_distance(2))  # 20, 60
    print(binary_tree.nodes_at_distance(0))  # 10
    print(binary_tree.nodes_at_distance(1))  # 30
    print(binary_tree.nodes_at_distance(3))  # 50
    # print(binary_tree.nodes_at_distance(-1))  # Exception - Illegal Argument
    # print(binary_tree.nodes_at_distance(100))  # Exception - Illegal Argument
