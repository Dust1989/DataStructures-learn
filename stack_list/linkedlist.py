class LinkedList:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add_start_to_list(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node

    def remove_start_from_list(self):
        marker = self.__root

        if marker is None:
            raise BaseException("There is not thing to remove")

        if marker.get_next() is None:
            self.__root = None
            return marker

        self.__root = marker.get_next()
        return marker

    def find(self, text):
        marker = self.__root

        while marker:
            if marker.text == text:
                return marker
            marker = marker.get_next()
        raise LookupError(f"Text {text} was not found in the linked list.")

    def print_list(self):
        marker = self.__root

        while marker:
            marker.print_details()
            marker = marker.get_next()

    def get_size(self):
        count = 0
        marker = self.__root
        while marker:
            count += 1
            marker = marker.get_next()
        return count