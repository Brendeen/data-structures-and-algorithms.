from data_structures.kary_tree import KaryTree


def fizz_buzz_tree(tree):
    if tree.root is None:
        return None
    fizzytree = KaryTree(tree)

    def fizz_buzz_helper(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"
        print("Node value", node.value)

    def traverse(node):
        # if node is None:
        #     return

        fizz_buzz_helper(node)
        for child in node.children:
            traverse(child)

    traverse(fizzytree.root)
    return fizzytree
