from typing import List, Dict, Tuple, Mapping

from leetcode.binary_tree.TreeNode import TreeNode


def gen_tree(node_list: List[List[int]]) -> TreeNode:
    node_mapper = {}
    root = None

    for nodes in node_list:
        left, node_map = __gen_node(nodes[1], node_mapper)
        node_mapper = node_mapper | node_map

        right, node_map = __gen_node(nodes[2], node_mapper)
        node_mapper = node_mapper | node_map

        head, node_map = __gen_node(nodes[0], node_mapper)
        node_mapper = node_mapper | node_map
        head.left = left
        head.right = right

        if not root:
            root = head

    return root


def __gen_node(val: int, node_mapper: Dict[int, TreeNode]) -> Tuple[TreeNode, Mapping[int, TreeNode]]:
    if val in node_mapper:
        return node_mapper[val], {}
    else:
        node = TreeNode.build(val)
        return node, {val: node}
