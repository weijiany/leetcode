from leetcode.binary_tree.maximum_depth_of_binary_tree.maximum_depth_of_binary_tree import Solution
from tests.binary_tree.common import gen_tree


def test_tree_depth1():
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

    actual = Solution().maxDepth(root)

    assert actual == 3


def test_tree_depth2():
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

    actual = Solution().maxDepth(root)

    assert actual == 3
