from typing import List, Optional

from .list_node import ListNode


def gen_list(vals: List[int]) -> Optional[ListNode]:
    if vals is []:
        return None

    head = ListNode(vals[0])
    cur = head
    for index in range(1, len(vals)):
        cur.next = ListNode(vals[index])
        cur = cur.next
    return head
