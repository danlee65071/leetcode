from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = float('inf')

        def dfs(node, depth):
            if node is None:
                return
            if node.left is None and node.right is None:
                nonlocal min_depth
                min_depth = min(min_depth, depth)
                return
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

        dfs(root, 1)
        return min_depth if min_depth != float('inf') else 0
