class LinkedList:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_to_list(self, node):
        # if node is None and self.__root.get_next() is None:
        #     self.__root = node
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def clear_list(self):
        if self.__root and self.__root.get_next() is None:
            root = self.__root
            self.__root = None
            return root

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def find(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Name {} was not found in the linked list.".format(name))