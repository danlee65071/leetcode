class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # # top-down
        # memo = dict()

        # def dp(i, j):
        #     if i >= len(text1) or j >= len(text2):
        #         return 0
        #     if memo.get((i, j)) is None:
        #         if text1[i] == text2[j]:
        #             memo[(i, j)] = dp(i+1, j+1) + 1
        #         else:
        #             memo[(i, j)] = max(dp(i+1, j), dp(i, j+1))
        #     return memo[(i, j)]
        # return dp(0, 0)
        # bottom-up
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, - 1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]


solution = Solution()
text1 = "abcde"
text2 = "ace"
assert solution.longestCommonSubsequence(text1, text2) == 3
