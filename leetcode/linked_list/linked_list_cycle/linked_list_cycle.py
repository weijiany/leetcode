from leetcode.linked_list.list_node import ListNode


# https://leetcode.cn/problems/linked-list-cycle/


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
