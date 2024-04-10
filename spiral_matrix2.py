from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[1] * n for _ in range(n)]
        num = 1
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        while left <= right:
            # left to right
            for it in range(left, right+1):
                matrix[top][it] = num
                num += 1
            top += 1
            # top to bottom
            for it in range(top, bottom+1):
                matrix[it][right] = num
                num += 1
            right -= 1
            # right to left
            for it in range(right, left-1, -1):
                matrix[bottom][it] = num
                num += 1
            bottom -= 1
            # bottom to top
            for it in range(bottom, top-1, -1):
                matrix[it][left] = num
                num += 1
            left += 1
        return matrix


solution = Solution()
n = 3
assert solution.generateMatrix(n) == [[1,2,3],[8,9,4],[7,6,5]]
n = 1
assert solution.generateMatrix(n) == [[1]]
