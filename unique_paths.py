class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                board[i][j] = board[i][j-1] + board[i-1][j]
        return board[m-1][n-1]


solution = Solution()
m = 3
n = 7
assert solution.uniquePaths(m, n) == 28
m = 3
n = 2
assert solution.uniquePaths(m, n) == 3
m = 1
n = 1
assert solution.uniquePaths(m, n) == 1
