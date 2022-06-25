from typing import List, Optional

from leetcode.binary_tree.TreeNode import TreeNode


# https://leetcode.cn/problems/binary-tree-preorder-traversal/


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        while root is not None or len(stack) != 0:
            if root:
                stack.append(root)
                result.append(root.val)
                root = root.left
            else:
                root = stack.pop().right

        return result
