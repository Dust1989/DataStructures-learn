class MyQueue:
    def __init__(self):
        self.__root = None
        self.__size = 0

    def push(self, node):
        if self.__root:
            node.set_next(self.__root)
        self.__root = node
        self.__size += 1

    def get_root(self):
        return self.__root

    def get_size(self):
        return self.__size

    """
    这个方法有问题， 待会再解决
    """
    def pop(self):
        marker = self.__root
        if self.__size == 0:
            raise BaseException("Nothing to be pop!")
        while marker.get_next():
            marker = marker.get_next()
        self.__size -= 1
        return marker

    def print_queue(self):
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
