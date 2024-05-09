from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = []

        def dfs(root, cur_sum, cur_path):
            if root is None:
                return
            if root.left is None and root.right is None:
                if cur_sum + root.val == targetSum:
                    cur_path.append(root.val)
                    paths.append(cur_path.copy())
                    cur_path.pop()
                return
            cur_path.append(root.val)
            dfs(root.left, cur_sum+root.val, cur_path)
            dfs(root.right, cur_sum+root.val, cur_path)
            cur_path.pop()

        dfs(root, 0, [])
        return paths
