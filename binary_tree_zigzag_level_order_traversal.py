from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q: deque = deque()
        zigzag_order: List[List[int]] = []
        layer: int = 0
        q += [root]
        while q:
            layer_order: List[int] = []
            len_q: int = len(q)
            for _ in range(len_q):
                node: TreeNode = q.popleft()
                if node is not None:
                    layer_order.append(node.val)
                    q += [node.left]
                    q += [node.right]
            if layer_order:
                zigzag_order.append(layer_order if layer % 2 == 0 else layer_order[::-1])
            layer += 1
        return zigzag_order
