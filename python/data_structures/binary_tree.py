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


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
