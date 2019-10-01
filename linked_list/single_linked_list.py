class SingleLinkedList(object):
    """
    simple implimentation of a linked singly linked list
    """

    def __init__(self):
        """
        initializes a new node with none values
        """

        self.next = None
        self.data = None

    def set_value(self,
                  value):
        """
        sets the data value of the current node
        """

        self.data = value

    def get_value(self):
        """
        returns the value of the current node
        """

        return self.data

    def set_next(self,
                 next_node):
        """
        sets the next node
        """

        self.next = next_node

    def get_next(self):
        """
        returns the next node
        """

        return self.next

    def has_next(self):
        """
        returns boolean if the current node has a next node or not
        """

        if self.next:
            return True

        return False
