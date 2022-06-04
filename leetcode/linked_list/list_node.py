class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next

    def __repr__(self) -> str:
        return str(self.val)
