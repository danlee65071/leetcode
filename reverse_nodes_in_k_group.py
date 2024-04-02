from typing import Tuple, Optional


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
    def reverseGroup(self, start_node: ListNode, end_node: ListNode) -> Tuple[ListNode]:
        prev_node: ListNode = start_node.next
        next_node: ListNode = end_node.next
        cur_node: ListNode = start_node
        while cur_node is not end_node:
            cur_node.next = next_node
            next_node = cur_node
            cur_node = prev_node
            prev_node = prev_node.next
        cur_node.next = next_node
        return cur_node, start_node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        cur_node: ListNode = head
        prev_node: ListNode = head
        while cur_node is not None:
            start_node: ListNode = cur_node
            end_node: ListNode = cur_node
            num_nodes: int = 1
            while end_node.next is not None and num_nodes < k:
                end_node = end_node.next
                num_nodes += 1
            if num_nodes == k:
                if prev_node is head:
                    head, prev_node = self.reverseGroup(start_node, end_node)
                else:
                    prev_node.next, prev_node = self.reverseGroup(start_node, end_node)
                cur_node = prev_node.next
            else:
                break
        return head


s = Solution()
print('Test1')
l = create_list([1, 2, 3, 4, 5, 6])
print_list(s.reverseKGroup(l, k=3))
print('Test2')
l = create_list([1, 2, 3, 4, 5])
print_list(s.reverseKGroup(l, k=2))
print('Test3')
l = create_list([1, 2, 3, 4, 5])
print_list(s.reverseKGroup(l, k=3))
print('Test4')
l = create_list([])
print_list(s.reverseKGroup(l, k=3))
print('Test5')
l = create_list([1, 2])
print_list(s.reverseKGroup(l, k=3))
print('Test6')
l = create_list([1, 2, 3, 4, 5])
print_list(s.reverseKGroup(l, k=1))
