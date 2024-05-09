from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root_id = len(nums) // 2
        root = TreeNode(nums[root_id])
        root.left = self.sortedArrayToBST(nums[:root_id])
        root.right = self.sortedArrayToBST(nums[root_id+1:])
        return root
