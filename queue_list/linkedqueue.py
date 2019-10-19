from linked_list.LinkedList import LinkedList


class LinkedQueue:

    def __init__(self):
        self.__linked_list = LinkedList()

    def get_root(self):
        return self.__linked_list.get_root()

    def push(self, node):
        self.__linked_list.add_to_list(node)

    def pop(self):
        marker = self.__linked_list.get_root()
        if marker is None:
            raise BaseException("Nothing to be pop!")
        while marker.get_next():
            if marker.get_next().get_next() is None:
                pop_node = marker.get_next()
                marker.set_next(None)
                return pop_node
            marker = marker.get_next()
        return self.__linked_list.clear_list()

    def print_queue(self):
        self.__linked_list.print_list()

    def get_size(self):
        marker = self.__linked_list.get_root()
        count = 0
        while marker:
            count += 1
            marker = marker.get_next()
        return count

    def find(self, name):
        return self.__linked_list.find(name)