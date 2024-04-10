from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == 0 and j == 0:
                    obstacleGrid[i][j] = 1
                elif i == 0:
                    obstacleGrid[i][j] = 1 if obstacleGrid[i][j-1] != 0 else 0
                elif j == 0:
                    obstacleGrid[i][j] = 1 if obstacleGrid[i-1][j] != 0 else 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
        return obstacleGrid[m-1][n-1]


solution = Solution()
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
assert solution.uniquePathsWithObstacles(obstacleGrid) == 2
obstacleGrid = [[0,1],[0,0]]
assert solution.uniquePathsWithObstacles(obstacleGrid) == 1
obstacleGrid = [[1,0]]
assert solution.uniquePathsWithObstacles(obstacleGrid) == 0
