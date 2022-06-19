from typing import List

import pytest

from leetcode.linked_list.add_two_numbers.add_two_numbers import Solution
from tests.linked_list.common import gen_list


@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 2, 3], [1, 2, 3], [2, 4, 6]),
    ([9, 1], [1, 9], [0, 1, 1]),
    ([9, 1], [9], [8, 2]),
    ([9, 9], [9, 9, 9], [8, 9, 0, 1])
])
def test_add_two_numbers(l1: List[int], l2: List[int], expected: List[int]):
    head = Solution().addTwoNumbers(gen_list(l1), gen_list(l2))
    expected = gen_list(expected)

    while expected and head:
        assert expected.val == head.val
        expected = expected.next
        head = head.next
