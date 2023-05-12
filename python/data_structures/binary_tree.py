class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        result = []

        def traverse(node):
            if not node:
                return

            result.append(node.value)
            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return result

    def in_order(self):
        result = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            result.append(node.value)
            traverse(node.right)

        traverse(self.root)
        return result

    def post_order(self):
        result = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            traverse(node.right)
            result.append(node.value)

        traverse(self.root)
        return result

    def find_maximum_value(self):
        if not self.root:
            return None

        max_val = self.root.value

        def traverse(node):
            nonlocal max_val
            if not node:
                return

            if node.value > max_val:
                max_val = node.value

            traverse(node.left)
            traverse(node.right)

        traverse(self.root)
        return max_val


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
