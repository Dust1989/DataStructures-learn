from btree_list.binary_tree import BinaryTree
from btree_list.node import Node

names = (("Jose", 2), ("Rolf", 1), ("Anna", 3), ("Dust", 28), ("James", 23), ("Curry", 30), ("Kobe", 24))

nodes = [Node(name, value) for name, value in names]

binary_tree = BinaryTree()

for node in nodes:
    binary_tree.add(node)

binary_tree.print_inorder()
