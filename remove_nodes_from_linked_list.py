from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack: List[ListNode] = []
        list_it: ListNode = head
        while list_it is not None:
            while stack and stack[-1].val < list_it.val:
                stack.pop()
            stack.append(list_it)
            list_it = list_it.next
        head = stack[0]
        list_it = head
        for i in range(1, len(stack)):
            list_it.next = stack[i]
            list_it = list_it.next
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
        print(head.val, end=' ')
        head = head.next
    print()


solution: Solution = Solution()
head: ListNode = create_list([5,2,13,3,8])
print_list(solution.removeNodes(head))
head: ListNode = create_list([1,1,1,1])
print_list(solution.removeNodes(head))
