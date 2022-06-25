from leetcode.binary_tree.binary_tree_preorder_traversal.binary_tree_preorder_traversal import Solution
from tests.binary_tree.common import gen_tree


def test_pre_order_traversal1():
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

    actual = Solution().preorderTraversal(root)

    assert actual == [1, 2, 4, 5, 3]


def test_pre_order_traversal2():
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

    actual = Solution().preorderTraversal(root)

    assert actual == [1, 2, 3]
