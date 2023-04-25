from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError


class PseudoQueue:
    def __init__(self):
        self.stack_a = Stack()
        self.stack_b = Stack()

    def enqueue(self, value):
        self.stack_a.push(value)

    def dequeue(self):
        # If both stacks are empty, raise an error
        if self.stack_a.is_empty() and self.stack_b.is_empty():
            raise InvalidOperationError("Cannot dequeue from empty queue")

        # If the second stack is empty, move all elements from the first stack to it
        if self.stack_b.is_empty():
            while not self.stack_a.is_empty():
                self.stack_b.push(self.stack_a.pop())

        # Pop and return the top element from the second stack
        return self.stack_b.pop()


if __name__ == "__main__":
    pass
