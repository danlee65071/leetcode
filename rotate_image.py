from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right-left):
                top, bottom = left, right
                tmp = matrix[top][left+i]
                matrix[top][left+i] = matrix[bottom-i][left]
                matrix[bottom-i][left] = matrix[bottom][right-i]
                matrix[bottom][right-i] = matrix[top+i][right]
                matrix[top+i][right] = tmp
            left += 1
            right -= 1


solution = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix)
assert matrix == [[7,4,1],[8,5,2],[9,6,3]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(matrix)
assert [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
