from typing import List

import pytest

from leetcode.linked_list.reorder_list.reorder_list import Solution
from tests.linked_list.common import gen_list


@pytest.mark.parametrize("vals, expected", [
    ([1, 2, 3, 4], [1, 4, 2, 3]),
    ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),
])
def test_should_reorder(vals: List[int], expected: List[int]):
    head = gen_list(vals)
    Solution().reorderList(head)

    r = []
    while head is not None:
        r.append(head.val)
        head = head.next

    assert r == expected
