from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # # top-down
        # memo = dict()

        # def dp(i):
        #     if i < 2:
        #         return 0
        #     if memo.get(i) is None:
        #         memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        #     return memo[i]
        # return dp(len(cost))
        # bottom-up
        if len(cost) < 2:
            return 0
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[len(cost)]


solution = Solution()
cost = [10,15,20]
assert solution.minCostClimbingStairs(cost) == 15
cost = [1,100,1,1,1,100,1,1,100,1]
assert solution.minCostClimbingStairs(cost) == 6
