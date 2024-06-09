from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # top-down
        memo = dict()

        def dp(i, cur_color):
            if i == len(costs):
                return 0
            if memo.get((i, cur_color)) is None:
                memo[(i, cur_color)] = min(dp(i+1, (cur_color-1) % 3), dp(i+1, (cur_color+1) % 3)) + costs[i][cur_color]
            return memo[(i, cur_color)]

        for color in range(3):
            dp(0, color)
        return min(memo[(0, 0)], memo[(0, 1)], memo[(0, 2)])


solution = Solution()
costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
assert solution.minCost(costs) == 10
