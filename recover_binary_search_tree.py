from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev_node: TreeNode = TreeNode(float('-inf'))
        first_swap_node: Optional[TreeNode] = None
        middle_swap_node: Optional[TreeNode] = None
        last_swap_node: Optional[TreeNode] = None

        def recover(cur_node: Optional[TreeNode]) -> None:
            if cur_node is None:
                return
            recover(cur_node.left)
            nonlocal prev_node
            nonlocal first_swap_node
            nonlocal middle_swap_node
            nonlocal last_swap_node
            if prev_node is not None and cur_node.val < prev_node.val:
                if first_swap_node is None:
                    first_swap_node = prev_node
                    middle_swap_node = cur_node
                else:
                    last_swap_node = cur_node
            prev_node = cur_node
            recover(cur_node.right)

        recover(root)
        if last_swap_node is None:
            first_swap_node.val, middle_swap_node.val = middle_swap_node.val, first_swap_node.val
        else:
            first_swap_node.val, last_swap_node.val = last_swap_node.val, first_swap_node.val
        return root
