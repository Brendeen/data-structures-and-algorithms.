from data_structures.binary_tree import BinaryTree


def tree_intersection(tree1, tree2):
    values1 = {}
    values2 = {}

    def traverse(node, values):
        if not node:
            return

        values[node.value] = True
        traverse(node.left, values)
        traverse(node.right, values)

    traverse(tree1.root, values1)
    traverse(tree2.root, values2)

    common_values = []
    for value in values1:
        if value in values2:
            common_values.append(value)

    if common_values:
        print(common_values)
        return common_values
    else:
        print("No like values.")
        return None
