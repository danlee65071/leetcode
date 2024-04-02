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
        print(head.val)
        head = head.next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_len = 0
        tmp_head = head
        while tmp_head is not None:
            list_len += 1
            tmp_head = tmp_head.next
        removed_idx = list_len - n
        if removed_idx == 0:
            head = head.next
        else:
            cur_idx = 0
            tmp_head = head
            while cur_idx < removed_idx - 1:
                tmp_head = tmp_head.next
                cur_idx += 1
            if tmp_head.next is not None:
                tmp_head.next = tmp_head.next.next
            else:
                tmp_head.next = None
        return head


s = Solution()

print('Test 1')
l1 = create_list([1, 2, 3, 4, 5])
n1 = 2
res1 = s.removeNthFromEnd(l1, n1)
print_list(res1)

print('Test 2')
l2 = create_list([1])
n2 = 1
res2 = s.removeNthFromEnd(l2, n2)
print_list(res2)

print('Test 3')
l3 = create_list([1, 2])
n3 = 1
res3 = s.removeNthFromEnd(l3, n3)
print_list(res3)
