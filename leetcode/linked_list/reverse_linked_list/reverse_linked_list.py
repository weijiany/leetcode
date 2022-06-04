from leetcode.linked_list.list_node import ListNode

# https://leetcode.cn/problems/reverse-linked-list/


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        result = None

        while current:
            next_loop_node = current.next
            current.next = result
            result = current
            current = next_loop_node

        return result
