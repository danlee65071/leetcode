from typing import List
from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # # top-down
        # @lru_cache(None)
        # def dfs(cur_amount: int) -> int:
        #     if cur_amount < 0:
        #         return -1
        #     if cur_amount == 0:
        #         return 0
        #     min_cost: float = float('inf')
        #     for coin in coins:
        #         res: int = dfs(cur_amount - coin)
        #         if res != -1:
        #             min_cost = min(min_cost, res + 1)
        #     return min_cost if min_cost != float('inf') else -1

        # return dfs(amount)
        
        # bottom-up
        dp: List[float] = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x-coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


solution: Solution = Solution()
coins = [1, 2, 5]
amount = 11
assert solution.coinChange(coins, amount) == 3
