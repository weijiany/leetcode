from typing import Optional, List

from leetcode.linked_list.list_node import ListNode


# https://leetcode.cn/problems/next-greater-node-in-linked-list/


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head, length = self.reverse_list_and_get_length(head)
        result, stack, index = [0] * length, [], length - 1

        while head:
            while len(stack) != 0 and stack[-1] <= head.val:
                stack.pop()
            result[index] = 0 if len(stack) == 0 else stack[-1]

            stack.append(head.val)
            index -= 1
            head = head.next

        return result

    def reverse_list_and_get_length(self, head: ListNode) -> (ListNode, int):
        current = head
        result = None
        length = 0

        while current:
            next_loop_node = current.next
            current.next = result
            result = current
            current = next_loop_node
            length += 1

        return result, length
