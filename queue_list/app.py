from queue_list.linkedqueue import LinkedQueue
from queue_list.node import Node
from queue_list.my_queue import MyQueue

# nba_menber = MyQueue()
#
#
#
# nba_menber.push(Node('Kobe', 123456))
# nba_menber.push(Node('James', 2568947))
# nba_menber.push(Node('Curry', 1984762))
# nba_menber.push(Node('Durant', 1862458))
# nba_menber.push(Node('Kwaii', 147635848))
#
# node_ = nba_menber.pop()
# node_.print_details()
# print(nba_menber.get_size())

names = ("James", 1234), ("Kobe", 3456), ("Curry", 7890)

nodes = [Node(name, telephone) for name, telephone in names]

my_queue = LinkedQueue()
for node in nodes:
    my_queue.push(node)

print(my_queue.get_size())
pop_node = my_queue.pop()
print(pop_node)
print(my_queue.get_size())
