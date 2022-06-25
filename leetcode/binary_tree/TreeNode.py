from dataclasses import dataclass
from typing import Optional


@dataclass
class TreeNode:
    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

    @classmethod
    def build(
            cls,
            val: Optional[int]
    ) -> Optional["TreeNode"]:
        return TreeNode(val) if val else None
