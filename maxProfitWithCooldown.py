from typing import List
from functools import lru_cache


class Solution:
    # top-down
    def maxProfit(self, prices: List[int]) -> int:

        @lru_cache(None)
        def dp(i, is_hold):
            if i >= len(prices):
                return 0
            if is_hold:
                return max(dp(i+1, is_hold), dp(i+2, False) + prices[i])
            return max(dp(i+1, is_hold), dp(i+1, True) - prices[i])

        return dp(0, False)

    # bottom-up
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices) + 2)]
        for i in range(len(prices) - 1, -1, -1):
            for is_hold in range(2):
                do_nothing = dp[i+1][is_hold]
                do_something = dp[i+2][0] + prices[i] if is_hold else dp[i+1][1] - prices[i]
                dp[i][is_hold] = max(do_nothing, do_something)
        return dp[0][0]


solution = Solution()
prices = [1, 2, 3, 0, 2]
assert solution.maxProfit(prices) == 3
