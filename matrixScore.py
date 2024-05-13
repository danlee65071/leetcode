from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for row in range(m):
            if grid[row][0] == 0:
                for col in range(n):
                    grid[row][col] = 0 if grid[row][col] else 1
        for col in range(n):
            col_count = 0
            for row in range(m):
                col_count += grid[row][col]
            if 2 * col_count < m:
                for row in range(m):
                    grid[row][col] = 0 if grid[row][col] else 1
        score = 0
        for row in range(m):
            for col in range(n):
                score += grid[row][col] << (n - 1 - col)
        return score


solution = Solution()
grid = [[0,1],[0,1],[0,1],[0,0]]
assert solution.matrixScore(grid) == 11
