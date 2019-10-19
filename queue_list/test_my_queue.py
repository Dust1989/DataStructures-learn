# import unittest
from unittest import TestCase
from queue_list.node import Node
from queue_list.my_queue import MyQueue


# run with "python -m unittest test_my_queue.py"


class TestLinkedList(TestCase):

    def test_node_creation(self):
        name = "Dust"
        telephone = 123345

        node = Node(name, telephone)

        self.assertEqual(name, node.name)
        self.assertEqual(telephone, node.telephone)

    def test_list_creation(self):
        my_queue = MyQueue()

        self.assertIsNone(my_queue.get_root())
        self.assertEqual(my_queue.get_size(), 0)

    def test_pop(self):
        names = ("James", 1234), ("Kobe", 3456), ("Curry", 7890)

        nodes = [Node(name, telephone) for name, telephone in names]

        my_queue = MyQueue()
        for node in nodes:
            my_queue.push(node)

        pop_node = my_queue.pop()
        self.assertEqual(pop_node, nodes[0])
        self.assertEqual(my_queue.get_size(), len(nodes)-1)

    def test_pop_zero(self):
        my_queue = MyQueue()

        with self.assertRaises(BaseException):
            my_queue.pop()

    def test_push(self):
        name = "Dust"
        telephone = 123456

        node = Node(name, telephone)
        my_queue = MyQueue()
        my_queue.push(node)

        self.assertEqual(my_queue.get_root(), node)

    def test_push_many_to_queue(self):
        names = ("James", 1234), ("Kobe", 3456), ("Curry", 7890)

        nodes = [Node(name, telephone) for name, telephone in names]

        my_queue = MyQueue()
        for node in nodes:
            my_queue.push(node)

        self.assertEqual(my_queue.get_size(), len(nodes))
        marker = my_queue.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(nodes[i], marker)
            marker = marker.get_next()

    def test_find_in_list(self):
        names = ("James", 1234), ("Kobe", 3456), ("Curry", 7890)

        nodes = [Node(name, telephone) for name, telephone in names]

        my_queue = MyQueue()
        for node in nodes:
            my_queue.push(node)

        marker = my_queue.get_root()
        for i in range(len(nodes) - 1, -1, -1):
            self.assertEqual(nodes[i], my_queue.find(marker.name))
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        my_queue = MyQueue()

        with self.assertRaises(LookupError):
            my_queue.find("Dust")
