from typing import Dict


class Solution:
    def numTrees(self, n: int) -> int:
        num_trees_dict: Dict[int, int] = {0: 1}
        for nodes in range(1, n+1):
            num_trees_in_nodes = 0
            for root in range(1, nodes+1):
                num_left_nodes = root - 1
                num_right_nodes = nodes - root
                num_trees_in_nodes += num_trees_dict[num_left_nodes] * num_trees_dict[num_right_nodes]
            num_trees_dict[nodes] = num_trees_in_nodes
        return num_trees_dict[n]


solution: Solution = Solution()
n: int = 3
assert solution.numTrees(n) == 5
