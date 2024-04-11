from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


solution = Solution()
grid = [[1,3,1],[1,5,1],[4,2,1]]
assert solution.minPathSum(grid) == 7
grid = [[1,2,3],[4,5,6]]
assert solution.minPathSum(grid) == 12
