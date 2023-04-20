from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return self.top.value

    def pop(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            value = self.top.value
            self.top = self.top.next
            self.length -= 1
            return value

    def peek(self):
        if self.top is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
