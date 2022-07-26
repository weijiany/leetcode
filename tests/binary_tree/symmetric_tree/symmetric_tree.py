from leetcode.binary_tree.TreeNode import TreeNode
from leetcode.binary_tree.symmetric_tree.symmetric_tree import Solution


def test_tree_is_symmetric():
    """
        1
       / \
      2   2
     /     \
    3       3
    """
    root = TreeNode(1)
    l2 = TreeNode(2)
    r2 = TreeNode(2)
    root.left = l2
    root.right = r2
    l3 = TreeNode(3)
    l2.left = l3
    r3 = TreeNode(3)
    r2.right = r3

    assert Solution().isSymmetric(root)


def test_tree_is_not_symmetric():
    """
        1
       /
      2
    """
    root = TreeNode(1)
    l2 = TreeNode(2)
    root.left = l2

    assert not Solution().isSymmetric(root)
