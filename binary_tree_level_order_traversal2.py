from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        q += [root]
        ans = []
        while q:
            tmp = []
            for _ in range(len(q)):
                node = q.popleft()
                if node is not None:
                    tmp.append(node.val)
                    q += [node.left]
                    q += [node.right]
            if tmp:
                ans.append(tmp)
        return ans[::-1]
