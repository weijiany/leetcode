from typing import Optional

from leetcode.binary_tree.TreeNode import TreeNode


# https://leetcode.cn/problems/symmetric-tree/

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._do_check(root.left, root.right)

    def _do_check(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False

        return left.val == right.val and \
               self._do_check(left.left, right.right) and \
               self._do_check(left.right, right.left)
