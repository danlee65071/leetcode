from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def FillList(arr: List[int]) -> ListNode:
    head = ListNode()
    tmp = head
    for it, val in enumerate(arr):
        tmp.val = val
        if it < len(arr) - 1:
            tmp.next = ListNode()
            tmp = tmp.next
    return head


def PrintList(list_node: ListNode) -> None:
    tmp_node = list_node
    while tmp_node is not None:
        print(f'{tmp_node.val} -> ', end='')
        tmp_node = tmp_node.next
    print('None')


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node1 = node2 = node_prev = None
        is_replace = False
        tmp = head
        while tmp is not None:
            if node1 is None:
                node1 = tmp
                tmp = tmp.next
            elif node2 is None:
                node2 = tmp
                tmp = tmp.next
            if node1 is not None and node2 is not None:
                node2.next, node1.next = node1, node2.next
                if node_prev is not None:
                    node_prev.next = node2
                if not is_replace:
                    is_replace = True
                    head = node2
                node_prev = node1
                tmp = node1.next
                node1 = node2 = None
        return head


s = Solution()
# test1
head = FillList([1, 2])
PrintList(s.swapPairs(head))
# test2
head = FillList([1, 2, 3, 4])
PrintList(s.swapPairs(head))
# test2
head = FillList([1])
PrintList(s.swapPairs(head))
