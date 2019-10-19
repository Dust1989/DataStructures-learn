from queue_list_su.linkedlist import LinkedList
from queue_list_su.node import Node
from queue_list_su.linkedqueue import LinkedQueue

names = ("Jose", "1234-356"), ("Rolf", "2345-1-53563-2"), ("Anna", "345623-16779-3"), ("Dust", "123456-16779-3")


nodes = [Node(name, phone) for name, phone in names]
#
# linked_list = LinkedList()
#
# for node in nodes:
#     linked_list.add_start_to_list(node)
#
#
# popped_node = linked_list.remove_end_from_list()
#
# print(popped_node)
# linked_list.print_list()
# popped_node = linked_list.remove_end_from_list()
#
# print(popped_node)
# linked_list.print_list()
#------------------------Queue-----------------

linked_queue = LinkedQueue()

for node in nodes:
    linked_queue.push(node)

print(len(linked_queue))

popped_node = linked_queue.pop()

print(len(linked_queue))
popped_node.print_details()
print(len(linked_queue))
linked_queue.print_details()