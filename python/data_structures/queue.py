from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front=None, tail=None):
        self.front = front
        self.tail = tail
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.tail is None:
            self.front = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self.front.value

    def dequeue(self):
        if self.front is None:
            self.tail = None
            raise InvalidOperationError("No queued values")
        value = self.front.value
        self.front = self.front.next
        self.length -= 1
        return value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError("No queued values")
        else:
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False


if __name__ == '__main__':
    pass
