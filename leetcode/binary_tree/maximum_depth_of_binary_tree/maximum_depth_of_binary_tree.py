from typing import Optional

from leetcode.binary_tree.TreeNode import TreeNode


# https://leetcode.cn/problems/maximum-depth-of-binary-tree/submissions/

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
