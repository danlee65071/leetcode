from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # top-down
        @lru_cache(None)
        def dp(i, is_hold):
            if i == len(prices):
                return 0
            if is_hold:
                return max(dp(i+1, is_hold), dp(i+1, False) + prices[i] - fee)
            return max(dp(i+1, is_hold), dp(i+1, True) - prices[i])

        return dp(0, False)


solution = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
assert solution.maxProfit(prices, fee) == 8
