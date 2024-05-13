from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for i in range(n):
            row = []
            for j in range(n):
                center_sub_matrix = (i+1, j+1)
                if center_sub_matrix[0] == 0 or center_sub_matrix[0] >= n-1 or \
                        center_sub_matrix[1] == 0 or center_sub_matrix[1] >= n-1:
                    continue
                max_num = grid[center_sub_matrix[0]-1][center_sub_matrix[1]-1]
                for k in range(center_sub_matrix[0]-1, center_sub_matrix[0]+2):
                    for z in range(center_sub_matrix[1]-1, center_sub_matrix[1]+2):
                        max_num = max(max_num, grid[k][z])
                row.append(max_num)
            if row:
                res.append(row)
        return res


solution = Solution()
grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
assert solution.largestLocal(grid) == [[9,9],[8,6]]
grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
assert solution.largestLocal(grid) == [[2,2,2],[2,2,2],[2,2,2]]
