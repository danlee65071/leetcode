from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        while left <= right:
            current = (left + right) // 2
            cur_i, cur_j = current // len(matrix[0]), current % len(matrix[0])
            if matrix[cur_i][cur_j] == target:
                return True
            elif matrix[cur_i][cur_j] > target:
                right = current - 1
            else:
                left = current + 1
        return False


solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
assert solution.searchMatrix(matrix, target) == True
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
assert solution.searchMatrix(matrix, target) == False
