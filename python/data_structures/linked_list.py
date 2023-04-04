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


class TargetError:
    linked = LinkedList()


if __name__ == "__main__":
    # print(LinkedList().head)
    # LinkedList().insert("apple")
    # print(LinkedList().head)
    pass

