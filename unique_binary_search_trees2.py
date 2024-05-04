from typing import List, Optional, Dict, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        trees_cache: Dict[Tuple[int, int], List[Optional[TreeNode]]] = dict()

        def generate(left_val: int, right_val: int) -> List[Optional[TreeNode]]:
            if trees_cache.get((left_val, right_val)) is not None:
                return trees_cache[(left_val, right_val)]
            if left_val > right_val:
                return [None]
            res: List[Optional[TreeNode]] = []
            for val in range(left_val, right_val+1):
                for left_tree in generate(left_val, val-1):
                    for right_tree in generate(val+1, right_val):
                        root: TreeNode = TreeNode(val, left_tree, right_tree)
                        res.append(root)
            trees_cache[(left_val, right_val)] = res
            return res

        return generate(1, n)


solution: Solution = Solution()
n: int = 2
res: List[Optional[TreeNode]] = solution.generateTrees(n)
