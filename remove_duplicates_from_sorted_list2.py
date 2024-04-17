from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy: ListNode = ListNode()
        dummy.next = head
        cur = dummy
        while cur:
            if cur.next and cur.next.next and cur.next.val == cur.next.next.val:
                tmp: ListNode = cur.next.next
                while tmp.next and tmp.val == tmp.next.val:
                    tmp = tmp.next
                cur.next = tmp.next
            else:
                cur = cur.next
        return dummy.next
