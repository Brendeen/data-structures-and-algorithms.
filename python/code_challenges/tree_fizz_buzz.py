from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node

karytree = KaryTree()


def fizz_buzz_tree(karytree):
    def fizz_buzz_helper(node):
        if node.value % 3 == 0 and node.value % 5 == 0:
            node.value = "FizzBuzz"
        elif node.value % 3 == 0:
            node.value = "Fizz"
        elif node.value % 5 == 0:
            node.value = "Buzz"

    def traverse(node):
        if node is None:
            return
        fizz_buzz_helper(node)
        for child in node.children:
            traverse(child)

    traverse(karytree.root)
    return karytree
