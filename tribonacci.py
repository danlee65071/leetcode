class Solution:
    def tribonacci(self, n: int) -> int:
#         # top-down
#         memo = dict()

#         def dp(i):
#             if i == 0:
#                 return 0
#             elif i == 1 or i == 2:
#                 return 1
#             if memo.get(i) is None:
#                 memo[i] = dp(i-1) + dp(i-2) + dp(i-3)
#             return memo[i]
#         return dp(n)
        # bottom-up
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]