from typing import List

import pytest

from linked_list.common import gen_list
from linked_list.next_greater_node_in_linked_list.next_greater_node_in_linked_list import Solution


@pytest.mark.parametrize("vals, expected", [
    ([2, 1, 5], [5, 5, 0]),
    ([2, 2, 5], [5, 5, 0]),
    ([2, 7, 4, 3, 5], [7, 0, 5, 5, 0]),
    ([1, 7, 1, 9], [7, 9, 9, 0]),
    ([1, 5, 7, 1, 9], [5, 7, 9, 9, 0]),
    ([1, 7, 5, 1, 9, 2, 5, 1], [7, 9, 9, 9, 0, 5, 0, 0]),
])
def test_should_reverse(vals: List[int], expected: List[int]):
    result = Solution().nextLargerNodes(gen_list(vals))
    assert result == expected
