import pytest
from code_challenges.tree_intersection import tree_intersection
from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue

# commented out tests and created new ones at the bottom


# def test_exists():
#     assert tree_intersection
#
#
# @pytest.mark.skip("TODO")
# def test_tree_intersection():
#
#     tree_a = BinaryTree()
#     values = [150, 100, 250, 75, 160, 200, 350, 125, 175, 300, 500]
#     add_values_to_empty_tree(tree_a, values)
#
#     tree_b = BinaryTree()
#     values = [42, 100, 100, 15, 160, 200, 350, 125, 175, 4, 500]
#     add_values_to_empty_tree(tree_b, values)
#
#     actual = tree_intersection(tree_a, tree_b)
#     expected = [125, 175, 100, 160, 500, 200, 350]
#
#     assert sorted(actual) == sorted(expected)
#
#
# def add_values_to_empty_tree(tree, values):
#     """
#     Helper function to add given values to BinaryTree
#     """
#     tree.root = Node(values.pop())
#     q = Queue()
#
#     q.enqueue(tree.root)
#
#     while values:
#         node = q.dequeue()
#         node.left = Node(values.pop())
#         node.right = Node(values.pop()) if values else None
#         q.enqueue(node.left)
#         q.enqueue(node.right)

def test_tree_intersection():
    # Create the binary trees for testing
    tree1 = BinaryTree(
        Node(1,
             Node(2,
                  Node(3),
                  Node(4)),
             Node(5,
                  Node(6),
                  Node(7))
             )
    )

    tree2 = BinaryTree(
        Node(5,
             Node(6,
                  Node(8),
                  Node(9)),
             Node(10,
                  Node(2),
                  Node(4))
             )
    )

    # Test case 1: Trees have common values
    result = tree_intersection(tree1, tree2)
    assert result == [2, 4, 5, 6]

    # Test case 2: Trees have no common values
    tree3 = BinaryTree(
        Node(1,
             Node(2,
                  Node(3),
                  Node(4)),
             Node(5,
                  Node(6),
                  Node(7))
             )
    )

    tree4 = BinaryTree(
        Node(8,
             Node(9),
             Node(10)
             )
    )

    result = tree_intersection(tree3, tree4)
    assert result is None

    # Test case 3: One tree is empty
    tree5 = BinaryTree()

    result = tree_intersection(tree5, tree4)
    assert result is None

    # Test case 4: Both trees are empty
    tree6 = BinaryTree()

    result = tree_intersection(tree5, tree6)
    assert result is None

