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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l_prev: ListNode = ListNode()
        l_prev.next = head
        left_node: ListNode = head
        it = 1
        while it != left:
            if it == left - 1:
                l_prev = left_node
            left_node = left_node.next
            it += 1
        right_node: ListNode = left_node
        r_prev: ListNode = l_prev
        while it != right:
            if it == right - 1:
                r_prev = right_node
            right_node = right_node.next
            it += 1
        while left_node != right_node:
            if left_node.next != right_node:
                left_node.next, right_node.next = right_node.next, left_node.next
            else:
                left_node.next, right_node.next = right_node.next, left_node
            if r_prev != left_node:
                if l_prev.next is head:
                    head, r_prev.next = right_node, left_node
                else:
                    l_prev.next, r_prev.next = right_node, left_node
            else:
                if l_prev.next is head:
                    head = right_node
                else:
                    l_prev.next = right_node
            l_prev = right_node
            left_node, right_node = right_node.next, r_prev
            r_prev = l_prev
            while r_prev.next != right_node:
                r_prev = r_prev.next
        return head


solution: Solution = Solution()
head: ListNode = create_list([1,2,3,4,5])
left: int = 2
right: int = 4
head: ListNode = solution.reverseBetween(head, left, right)
print_list(head)
head: ListNode = create_list([3,5])
left: int = 1
right: int = 2
head: ListNode = solution.reverseBetween(head, left, right)
print_list(head)
