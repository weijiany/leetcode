from leetcode.linked_list.linked_list_cycle_ii.linked_list_cycle_ii import Solution
from leetcode.linked_list.list_node import ListNode


def test_should_find_index_of_cycle_linked_list():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = n1

    assert Solution().detectCycle(n1) == n1


def test_should_return_none_whit_no_cycle_list():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2

    assert Solution().detectCycle(n1) is None


def test_should_return_none_whit_only_one_onde_list():
    n1 = ListNode(1)

    assert Solution().detectCycle(n1) is None
