from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        head_it: ListNode = head
        left: ListNode = ListNode()
        right: ListNode = ListNode()
        left_it: ListNode = left
        right_it: ListNode = right
        while head_it is not None:
            if head_it.val < x:
                left_it.next = head_it
                left_it = left_it.next
            else:
                right_it.next = head_it
                right_it = right_it.next
            head_it = head_it.next
        left_it.next = right.next
        right_it.next = None
        return left.next
