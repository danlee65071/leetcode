from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_list: List[List[int]] = []

        def dfs(node: Optional[TreeNode], layer: int) -> None:
            if node is None:
                return
            if len(level_list) < layer + 1:
                level_list.append([node.val])
            else:
                level_list[layer] += [node.val]
            dfs(node.left, layer+1)
            dfs(node.right, layer+1)

        dfs(root, 0)
        return level_list
