from typing import Optional, Tuple

from leetcode.linked_list.list_node import ListNode


# https://leetcode.cn/problems/add-two-numbers/


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = cursor = ListNode()
        carry_bit = 0
        while l1 or l2:
            l1_v, l1 = self.val_and_next(l1)
            l2_v, l2 = self.val_and_next(l2)
            val = l1_v + l2_v + carry_bit

            cursor.next = ListNode(val)
            carry_bit = 0
            if val >= 10:
                val -= 10
                cursor.next = ListNode(val)
                carry_bit = 1

            cursor = cursor.next

        if carry_bit != 0:
            cursor.next = ListNode(carry_bit)

        result = result.next
        return result

    def val_and_next(self, node: ListNode) -> Tuple[int, Optional[ListNode]]:
        if node:
            return node.val, node.next
        return 0, None
