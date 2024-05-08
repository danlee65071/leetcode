from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth: int = 0

        def dfs(root: Optional[TreeNode], depth: int):
            if root is None:
                nonlocal max_depth
                max_depth = max(max_depth, depth)
                return
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        dfs(root, 0)
        return max_depth
