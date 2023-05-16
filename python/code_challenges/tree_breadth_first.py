from data_structures.binary_tree import BinaryTree

bt = BinaryTree()


def breadth_first(bt):
    if not bt.root:
        return []

    tree_result = []
    queue = [bt.root]

    while queue:
        node = queue.pop(0)
        tree_result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return tree_result


