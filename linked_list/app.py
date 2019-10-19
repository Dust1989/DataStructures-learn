from linked_list.node import Node
from linked_list.LinkedList import LinkedList

nba_menber = LinkedList()

nba_menber.add_to_list(Node('aa', 'Kobe', 40))
nba_menber.add_to_list(Node('aa', 'James', 35))
nba_menber.add_to_list(Node('aa', 'Curry', 31))
nba_menber.add_to_list(Node('aa', 'Durant', 30))
nba_menber.add_to_list(Node('aa', 'Kwaii', 28))

# nba_menber.print_list()
nba_menber.find("James").print_details()
