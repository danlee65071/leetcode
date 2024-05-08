from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check_trees(first_tree: Optional[TreeNode], second_tree: Optional[TreeNode]) -> bool:
            if first_tree is None or second_tree is None:
                return True if first_tree is None and second_tree is None else False
            if first_tree.val != second_tree.val:
                return False
            return check_trees(first_tree.left, second_tree.left) and check_trees(first_tree.right, second_tree.right)

        return check_trees(p, q)
