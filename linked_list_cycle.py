from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow_node: ListNode = head
        fast_node: ListNode = head
        while (fast_node is not None) and (fast_node.next is not None):
            slow_node = slow_node.next
            fast_node = fast_node.next.next
            if fast_node == slow_node:
                return True
        return False


s = Solution()

list_node1 = ListNode(1)
print(s.hasCycle(list_node1))
