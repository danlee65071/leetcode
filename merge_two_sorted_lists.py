import copy
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_list(data) -> ListNode:
    head_list = None
    tmp_head = head_list
    for d in data:
        node = ListNode(d, None)
        if head_list is None:
            head_list = node
            tmp_head = head_list
        else:
            tmp_head.next = node
            tmp_head = tmp_head.next
    return head_list


def print_list(head: ListNode) -> None:
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = curr = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
            elif list1:
                curr.next = list1
                list1 = list1.next
            elif list2:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        return head.next


s = Solution()

print('Test1')
l1 = create_list([1, 2, 4])
l2 = create_list([1, 3, 4])
print_list(s.mergeTwoLists(l1, l2))

print('Test2')
l1 = create_list([])
l2 = create_list([])
print_list(s.mergeTwoLists(l1, l2))

print('Test3')
l1 = create_list([])
l2 = create_list([0])
print_list(s.mergeTwoLists(l1, l2))
