from copy import copy


def get_no_of_nodes_to_end(node):
    """
    a utility function to calculate the no of elements to
    end of the linked list from the current node
    """

    count = 0

    while node.has_next():
        node = node.get_next()
        count = count + 1

    return count


def add_element_at_end(head,
                       node):
    """
    adds a new node at the end of the linked list
    """

    last_element = traverse_to_end(head)
    last_element.next = node
    node.next = None


def traverse_to_end(head):
    """
    traverses to the last node in the linked list and returns it
    """

    node = copy(head)

    while node.has_next():
        node = node.get_next()

    return node


def add_element_at_a_position(head,
                              element,
                              position):
    """
    adds a new element to the linked list at the given position if it exists
    """

    if position == 0:
        head = add_element_at_beginning(head,
                                        element)
    else:

        try:
            node_before_position = traverse_to_position(head,
                                                        position - 1)
            insert_as_next_node(node_before_position,
                                element)
        except Exception:
            return False

    return True


def traverse_to_position(head,
                         position):
    """
    traverses to the element before the given
    """

    if position == 0:
        return head

    count = 0
    node = copy(head)

    while count < position:
        if node.has_next():
            node = node.get_next()
            count += 1
        else:
            raise Exception('position out of reach')

    return node


def insert_as_next_node(current_node,
                        new_node):
    """
    inserts the new node that needs to be inserted after the current node
    """

    if current_node.has_next():
        temp_holder = current_node.get_next()
        current_node.set_next(new_node)
        new_node.set_next(temp_holder)
    else:
        current_node.set_next(new_node)
        new_node.set_next(None)


def add_element_at_beginning(head,
                             element):
    """
    adds a new element at the beginning and returns it as the new head
    """

    element.set_next(head)

    return element
