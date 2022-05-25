from typing import Optional, List

from linked_list.list_node import ListNode


class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head, length = self.reverse_list_and_get_length(head)
        result, stack, index = [0] * length, [], length - 1

        while head is not None:
            cur = head.val
            if len(stack) == 0:
                result[index] = 0
            elif stack[-1] > cur:
                result[index] = stack[-1]
            else:
                while len(stack) != 0 and stack[-1] <= cur:
                    stack.pop()
                continue

            stack.append(cur)
            index -= 1
            head = head.next

        return result


    def reverse_list_and_get_length(self, head: ListNode) -> (ListNode, int):
        current = head
        result = None
        length = 0

        while current is not None:
            next_loop_node = current.next
            current.next = result
            result = current
            current = next_loop_node
            length += 1

        return result, length
