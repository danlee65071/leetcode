from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_tree(root: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            if root is None:
                return True
            if min_val >= root.val or max_val <= root.val:
                return False
            return check_tree(root.left, min_val, root.val) and check_tree(root.right, root.val, max_val)

        return check_tree(root, float('-inf'), float('inf'))
