from leetcode.linked_list.linked_list_cycle.linked_list_cycle import Solution
from leetcode.linked_list.list_node import ListNode


def test_should_find_index_of_cycle_linked_list():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = n1

    assert Solution().hasCycle(n1)


def test_should_return_none_whit_no_cycle_list():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2

    assert not Solution().hasCycle(n1)

