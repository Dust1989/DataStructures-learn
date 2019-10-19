class BinaryTree:
    def __init__(self):
        self.__root = None

    def get_root(self):
        return self.__root

    def add(self, node):

        if self.__root is None:
            self.__root = node
        else:
            """my solution"""
            # current_node = self.__root
            # if marker.value == node.value:
            #     raise ValueError("A node with that value already exists.")
            # while current_node.value > node.value:
            #     if current_node.get_left() is None:
            #         current_node.set_left(node)
            #         break
            #     current_node = current_node.get_left()
            # while current_node.value < node.value:
            #     if current_node.get_right() is None:
            #         current_node.set_right(node)
            #         break
            #     current_node = current_node.get_right()
            """tutorial solution"""
            marker = self.__root
            while marker:
                if marker.value == node.value:
                    raise ValueError("A node with that value already exists.")
                elif marker.value > node.value:
                    if marker.get_left() is None:
                        marker.set_left(node)
                        break
                    marker = marker.get_left()
                elif marker.value < node.value:
                    if marker.get_right() is None:
                        marker.set_right(node)
                        break
                    marker = marker.get_right()

    def find(self, value):
        marker = self.__root
        while marker:
            if marker.value == value:
                return marker
            elif marker.value > value:
                marker = marker.get_left()
            elif marker.value < value:
                marker = marker.get_right()
        raise LookupError("A node with value {} was not found.".format(value))

    def print_inorder(self):
        self.__print_inorder_r(self.__root)

    def __print_inorder_r(self, current_node):
        if not current_node:
            return
        self.__print_inorder_r(current_node.get_left())
        current_node.print_details()
        self.__print_inorder_r(current_node.get_right())