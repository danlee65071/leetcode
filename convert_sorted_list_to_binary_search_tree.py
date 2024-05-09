from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return
        if head.next is None:
            return TreeNode(head.val)
        fast, slow = head, head
        prev_slow = ListNode()
        prev_slow.next = head
        while fast and fast.next:
            slow = slow.next
            prev_slow = prev_slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.right = self.sortedListToBST(slow.next)
        prev_slow.next = None
        root.left = self.sortedListToBST(head)
        return root


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


solution = Solution()
head = create_list([-10,-3,0,5,9])
solution.sortedListToBST(head)
