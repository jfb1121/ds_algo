class DoublyLinkedList(object):
    """
    simple implimentation of a doubly
    linked list
    """

    def __init__(self,
                 data=None,
                 previous_node=None,
                 next_node=None):
        """
        initializes a new node with provided values or none
        """

        self.data = data
        self.previous_node = previous_node
        self.next_node = next_node

    def set_value(self,
                  value):
        """
        sets the value of the current node
        """

        self.data = value

    def set_previous(self,
                     previous_node):
        """
        sets the previous node to the current node
        """

        self.previous_node = previous_node

    def set_next(self,
                 next_node):
        """
        sets the next node to the current node
        """

        self.next_node = next_node

    def get_previous(self):
        """
        returns the previous node to the current node
        """

        return self.previous_node

    def get_next(self):
        """
        returns the next node to the current node
        """

        return self.next_node

    def has_next(self):
        """
        returns true / false if the current node has a next node or not
        """

        if self.next_node:
            return True

        return False

    def has_previous(self):
        """
        returns true / false if the current node has a previous node or not
        """

        if self.previous_node:
            return True

        return False
