from typing import Optional


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
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = tmp = None
        while cur is not None:
            tmp = cur.next
            cur.next = prev
            prev = cur
            if tmp is None:
                head = cur
            cur = tmp
        return head


s = Solution()
print('Test1')
l = create_list([1, 2, 3, 4, 5])
print_list(s.reverseList(l))
