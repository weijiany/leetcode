from leetcode.binary_tree.binary_tree_postorder_traversal.binary_tree_preorder_traversal import Solution
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

    actual = Solution().postorderTraversal(root)

    assert actual == [4, 5, 2, 3, 1]


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

    actual = Solution().postorderTraversal(root)

    assert actual == [3, 2, 1]


def test_pre_order_traversal3():
    root = gen_tree([])

    actual = Solution().postorderTraversal(root)

    assert actual == []
