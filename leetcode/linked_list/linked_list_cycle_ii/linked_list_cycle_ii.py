from typing import Optional

from leetcode.linked_list.list_node import ListNode


# https://leetcode.cn/problems/linked-list-cycle-ii/


class Solution:
    def detectCycle(self, head: ListNode) -> Optional[ListNode]:
        slow, fast = head, head

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        if fast is None or fast.next is None:
            return None

        while True:
            if head == slow:
                return head
            head = head.next
            slow = slow.next
