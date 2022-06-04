from typing import List

import pytest

from leetcode.linked_list.reverse_linked_list.reverse_linked_list import Solution
from tests.linked_list.common import gen_list


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
