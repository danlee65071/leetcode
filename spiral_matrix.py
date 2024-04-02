from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left_margin, down_margin = len(matrix[0]), len(matrix)
        rigth_margin, up_margin = -1, 0
        i, j = 0, 0
        res = []
        while len(res) < len(matrix) * len(matrix[0]):
            while j < left_margin and len(res) < len(matrix) * len(matrix[0]):
                res.append(matrix[i][j])
                j += 1
            i += 1
            j -= 1
            while i < down_margin and len(res) < len(matrix) * len(matrix[0]):
                res.append(matrix[i][j])
                i += 1
            j -= 1
            i -= 1
            left_margin -= 1
            down_margin -= 1
            while j > rigth_margin and len(res) < len(matrix) * len(matrix[0]):
                res.append(matrix[i][j])
                j -= 1
            i -= 1
            j += 1
            while i > up_margin and len(res) < len(matrix) * len(matrix[0]):
                res.append(matrix[i][j])
                i -= 1
            j += 1
            i += 1
            rigth_margin += 1
            up_margin += 1
        return res


solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.spiralOrder(matrix))
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(solution.spiralOrder(matrix))
