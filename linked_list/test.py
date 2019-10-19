# import unittest
from unittest import TestCase
from linked_list.node import Node
from linked_list.LinkedList import LinkedList

# run with "python -m unittest test_my_queue.py"


class TestLinkedList(TestCase):

    def test_node_creation(self):
        name = "Dust"
        matric = "1234"
        year = 3

        node = Node(matric, name, year)

        self.assertEqual(name, node.name)
        self.assertEqual(matric, node.matric)
        self.assertEqual(year, node.year)

    def test_list_creation(self):
        linked_list = LinkedList()

        self.assertIsNone(linked_list.get_root())

    def test_add_to_list(self):
        name = "Dust"
        matric = "1234"
        year = 3

        node = Node(matric, name, year)
        linked_list = LinkedList()
        linked_list.add_to_list(node)

        self.assertEqual(linked_list.get_root(), node)

    def test_add_many_to_list(self):
        names = ("James", "1234", 10), ("Kobe", "3456", 20), ("Curry", "7890", 8)

        nodes = [Node(matric, name, year) for name, matric, year in names]

        linked_list = LinkedList()
        for node in nodes:
            linked_list.add_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(nodes[i], marker)
            marker = marker.get_next()

    def test_find_in_list(self):
        names = ("James", "1234", 10), ("Kobe", "3456", 20), ("Curry", "7890", 8)

        nodes = [Node(matric, name, year) for name, matric, year in names]

        linked_list = LinkedList()
        for node in nodes:
            linked_list.add_to_list(node)

        marker = linked_list.get_root()
        for i in range(len(nodes)-1, -1, -1):
            self.assertEqual(nodes[i], linked_list.find(marker.name))
            marker = marker.get_next()

    def test_find_missing_in_list(self):
        linked_list = LinkedList()

        with self.assertRaises(LookupError):
            linked_list.find("Dust")


