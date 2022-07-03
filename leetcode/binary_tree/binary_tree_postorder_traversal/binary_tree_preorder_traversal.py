from typing import List, Optional

from leetcode.binary_tree.TreeNode import TreeNode


# https://leetcode.cn/problems/binary-tree-postorder-traversal/


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        stack: List[TreeNode] = [root]
        pre_node: Optional[TreeNode] = None

        while len(stack) != 0:
            root = stack[-1]
            if (root.left is None and root.right is None) or \
                    (pre_node is not None and (pre_node == root.left or pre_node == root.right)):
                result.append(stack.pop().val)
                pre_node = root
            else:
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return result
