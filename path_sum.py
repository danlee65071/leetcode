from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, cur_sum):
            if root is None:
                return False
            if root.left is None and root.right is None:
                if cur_sum + root.val == targetSum:
                    return True
                return False
            return dfs(root.left, cur_sum+root.val) or dfs(root.right, cur_sum+root.val)
        return dfs(root, 0)
