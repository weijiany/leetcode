from linked_list.list_node import ListNode

# https://leetcode.cn/problems/reorder-list/


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        length: int = self.len(head)
        left: ListNode = head

        for _ in range(length // 2 - 1):
            head = head.next
        right: ListNode = self.reverse(head.next)
        head.next = None

        cursor = ListNode()
        while left or right:
            cursor, left = self.change_node(cursor, left)
            cursor, right = self.change_node(cursor, right)

    def change_node(self, head: ListNode, sub_node: ListNode) -> (ListNode, ListNode):
        if sub_node:
            head.next = sub_node
            sub_node = sub_node.next
            head = head.next
        return head, sub_node

    def len(self, head: ListNode) -> int:
        length: int = 0
        while head:
            length += 1
            head = head.next
        return length

    def reverse(self, head: ListNode) -> ListNode:
        result = None
        current = head
        while current:
            next_loop_node = current.next
            current.next = result
            result = current
            current = next_loop_node
        return result
