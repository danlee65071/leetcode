from typing import List
from functools import lru_cache


class Solution:
    # top-down
    def maxProfit(self, k: int, prices: List[int]) -> int:

        @lru_cache(None)
        def dp(i, remain_k, is_hold):
            if i == len(prices) or remain_k == 0:
                return 0
            if is_hold:
                return max(dp(i+1, remain_k, is_hold), dp(i+1, remain_k-1, False) + prices[i])
            return max(dp(i+1, remain_k, is_hold), dp(i+1, remain_k, True) - prices[i])

        return dp(0, k, 0)

    # bottom-up
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0] * 2 for _ in range(k+1)] for __ in range(len(prices) + 1)]
        for i in range(len(prices) - 1, -1, -1):
            for cur_k in range(1, k+1):
                for hold in range(2):
                    do_nothing = dp[i+1][cur_k][hold]
                    do_something = 0
                    if hold:
                        do_something = dp[i+1][cur_k-1][0] + prices[i]
                    else:
                        do_something = dp[i+1][cur_k][1] - prices[i]
                    dp[i][cur_k][hold] = max(do_nothing, do_something)
        return dp[0][k][0]


solution = Solution()
k = 2
prices = [3, 3, 5, 0, 0, 3, 1, 4]
assert solution.maxProfit(k, prices) == 6
