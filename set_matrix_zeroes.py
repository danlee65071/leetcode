from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        set_zeroes_cols = set()
        set_zeroes_rows = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    set_zeroes_rows.add(i)
                    set_zeroes_cols.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in set_zeroes_rows or j in set_zeroes_cols:
                    matrix[i][j] = 0


solution = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
solution.setZeroes(matrix)
assert matrix == [[1,0,1],[0,0,0],[1,0,1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
solution.setZeroes(matrix)
assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
