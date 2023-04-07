
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        new_node = Node(value)
        # If the linked list is empty, make the new node the head node
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the end of the linked list
        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        # Append the new node to the end of the linked list
        last_node.next = new_node

    def insert_before(self, target_value, new_value):
        if self.head is None:
            raise TargetError("invalid value: " + target_value)

        if self.head.value == target_value:
            self.insert(new_value)
            return

        current = self.head
        while current.next is not None:
            if current.next.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise TargetError("invalid value: " + target_value)

    def insert_after(self, target_value, new_value):
        if self.head is None:
            raise TargetError(target_value + " does not exist")

        current = self.head
        while current is not None:
            if current.value == target_value:
                new_node = Node(new_value)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

        raise TargetError(target_value + " does not exist")

    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False

    def __str__(self):
        current_node = self.head
        string = ""
        if current_node is None:
            return "NULL"
        # elif current_node is self.head:
        #     return "{ " + current_node.value + " } -> NULL"
        # elif current_node is self.head.next:
        #     return "{ " + current_node.value + " } -> { " + current_node.next.value + " } -> NULL"
        else:
            string = "{ " + current_node.value + " }"
            current_node = current_node.next
            while current_node:
                string += " -> { " + current_node.value + " }"
                current_node = current_node.next
            string += " -> NULL"
            return string


class TargetError(Exception):
    pass


if __name__ == "__main__":
    # print(LinkedList().head)
    # LinkedList().insert("apple")
    # print(LinkedList().head)
    pass

