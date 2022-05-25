from linked_list.list_node import ListNode

# Definition for singly-linked list.
# https://leetcode.cn/problems/reverse-linked-list/


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        result = None

        while current is not None:
            next_loop_node = current.next
            current.next = result
            result = current
            current = next_loop_node

        return result
