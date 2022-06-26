from typing import Optional, List

from leetcode.binary_tree.TreeNode import TreeNode


# https://leetcode.cn/problems/binary-tree-inorder-traversal/


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []

        while root is not None or len(stack) != 0:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result
