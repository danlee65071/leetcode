from typing import List, Tuple


class Solution:
    def getUpDiagOrder(self, mat: List[List[int]], i: int, j: int) -> Tuple[List[int], int, int]:
        res = []
        res.append(mat[i][j])
        while i > 0 and j < len(mat[0]) - 1:
            i -= 1
            j += 1
            res.append(mat[i][j])
        return res, i, j

    def getDownDiagOrder(self, mat: List[List[int]], i: int, j: int) -> Tuple[List[int], int, int]:
        res = []
        res.append(mat[i][j])
        while i < len(mat) - 1 and j > 0:
            i += 1
            j -= 1
            res.append(mat[i][j])
        return res, i, j

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        it = 0
        i, j = 0, 0
        while i != len(mat) - 1 or j != len(mat[0]) - 1:
            add_res, i, j = self.getUpDiagOrder(mat, i, j) if it % 2 == 0 else self.getDownDiagOrder(mat, i, j)
            res += add_res
            if i == 0 or i == len(mat) - 1:
                if j == len(mat[0]) - 1:
                    i += 1
                else:
                    j += 1
            elif j == 0 or j == len(mat[0]) - 1:
                i += 1
            it += 1
        res.append(mat[i][j])
        return res


solution = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(solution.findDiagonalOrder(mat))
mat = [[1,2],[3,4]]
print(solution.findDiagonalOrder(mat))
mat = [[1,2,3,4], [5,6,7,8]]
print(solution.findDiagonalOrder(mat))
mat = [[0]]
print(solution.findDiagonalOrder(mat))
