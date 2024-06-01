from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(len(coins) - 1, -1, -1):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[amount]
