from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 0:
            return head
        tail = head
        list_len = 1
        while tail.next is not None:
            tail = tail.next
            list_len += 1
        if k % list_len == 0:
            return head
        if k > list_len:
            k = k % list_len
        tmp = head
        it = 0
        while tmp.next is not None and it < list_len - k:
            if it == list_len - k - 1:
                buf = tmp
                tmp = tmp.next
                buf.next = None
            else:
                tmp = tmp.next
            it += 1
        if list_len > 1:
            tail.next = head
        head = tmp
        return head


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


solution = Solution()
head = create_list([1,2,3,4,5])
k = 2
print_list(solution.rotateRight(head, k))
head = create_list([0,1,2])
k = 4
print_list(solution.rotateRight(head, k))
head = create_list([1])
k = 0
print_list(solution.rotateRight(head, k))
head = create_list([1])
k = 1
print_list(solution.rotateRight(head, k))
head = create_list([1, 2])
k = 0
print_list(solution.rotateRight(head, k))
head = create_list([1, 2])
k = 2
print_list(solution.rotateRight(head, k))
