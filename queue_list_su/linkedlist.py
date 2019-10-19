class LinkedList:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_end_from_list(self):
        marker = self.__root

        if marker is None:
            raise BaseException("There is not thing to remove")

        """
        My solution
        """
        # follow_node = marker.get_next()
        #
        # while follow_node:
        #     if follow_node.get_next() is None:
        #         marker.set_next(None)
        #         return follow_node
        #     marker = follow_node
        #     follow_node = follow_node.get_next()
        #
        # self.__root = None
        # return marker
        """
        Tutorials Solution
        """
        if not marker.get_next():
            self.__root = None
            return marker
        while marker:
            following_node = marker.get_next()
            if following_node:
                if following_node.get_next() is None:
                    marker.ser_root(None)
                    return following_node
            marker = following_node

    def find(self, name):
        marker = self.__root
        while marker:
            if marker.name == name:
                return marker
            marker = marker.get_next()
        raise LookupError("Name {} was not found in the linked list.".format(name))

    def print_list(self):
        marker = self.__root
        while marker:
            marker.print_details()
            marker = marker.get_next()

    def size(self):
        count = 0
        marker = self.__root
        while marker:
            count += 1
            marker = marker.get_next()
        return count