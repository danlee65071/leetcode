from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     tmp_stack: List[int] = []
    #     res_stack: List[int] = []
    #     remaider: int = 0
    #     cur_node: ListNode = head
    #     while cur_node is not None:
    #         tmp_stack.append(cur_node.val)
    #         cur_node = cur_node.next
    #     while len(tmp_stack) > 0:
    #         double_num: int = tmp_stack.pop() * 2 + remaider
    #         res_stack.append(double_num % 10)
    #         remaider = double_num // 10
    #     if remaider > 0:
    #         res_stack.append(remaider)
    #     dummy: ListNode = ListNode()
    #     cur_node = dummy
    #     while len(res_stack) > 0:
    #         cur_node.next = ListNode(res_stack.pop())
    #         cur_node = cur_node.next
    #     return dummy.next
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.val > 4:
            head = ListNode(0, head)
        cur_node: ListNode = head
        while cur_node:
            cur_node.val = 2 * cur_node.val % 10
            if cur_node.next and cur_node.next.val > 4:
                cur_node.val += 1
            cur_node = cur_node.next
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
head: ListNode = create_list([1,8,9])
print_list(solution.doubleIt(head))
