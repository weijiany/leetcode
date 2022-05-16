from typing import List, Optional

import pytest

from .list_node import ListNode
from .reverse_linked_list import Solution


def gen_list(vals: List[int]) -> Optional[ListNode]:
    if vals is []:
        return None

    head = ListNode(vals[0])
    cur = head
    for index in range(1, len(vals)):
        cur.next = ListNode(vals[index])
        cur = cur.next
    return head


@pytest.mark.parametrize("vals", (
    [[0, 1, 2]],
    [[0]],
    [[]],
))
def test_should_reverse(vals: List[int]):
    reverse_head = Solution().reverseList(gen_list(vals))
    r = []
    while reverse_head is not None:
        r.append(reverse_head.val)
        reverse_head = reverse_head.next

    vals.reverse()
    assert r == vals
