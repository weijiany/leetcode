from leetcode.binary_tree.binary_tree_inorder_traversal.binary_tree_inorder_traversal import Solution
from tests.binary_tree.common import gen_tree


def test_in_order_traversal1():
    """
        1
       / \
      2   3
     /\
    4  5
    """
    root = gen_tree([
        [1, 2, 3],
        [2, 4, 5]
    ])

    actual = Solution().inorderTraversal(root)

    assert actual == [4, 2, 5, 1, 3]


def test_in_order_traversal2():
    """
        1
       /
      2
       \
        3
    """
    root = gen_tree([
        [1, 2, None],
        [2, None, 3]
    ])

    actual = Solution().inorderTraversal(root)

    assert actual == [2, 3, 1]
