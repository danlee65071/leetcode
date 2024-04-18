from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        prev_hist = []
        max_area = 0
        for it, row in enumerate(matrix):
            if it == 0:
                cur_hist = [int(str_num) for str_num in row]
            else:
                cur_hist = [int(x) + int(y) if y != '0' else 0 for x, y in zip(prev_hist, row)]
            prev_hist = cur_hist
            hist_stack = []
            for pos, val in enumerate(cur_hist):
                if pos == 0 or val >= hist_stack[-1][1]:
                    hist_stack.append([pos, val])
                else:
                    while hist_stack and hist_stack[-1][1] > val:
                        prev_pos, prev_val = hist_stack.pop()
                        max_area = max(max_area, prev_val * (pos - prev_pos))
                    hist_stack.append([prev_pos, val])
            for (pos, val) in hist_stack:
                max_area = max(max_area, val * (len(matrix[0]) - pos))
        return max_area


solution = Solution()
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
assert solution.maximalRectangle(matrix) == 6
matrix = [["0"]]
assert solution.maximalRectangle(matrix) == 0
matrix = [["1"]]
assert solution.maximalRectangle(matrix) == 1
matrix = [["1"]]
assert solution.maximalRectangle(matrix) == 1
matrix = [["0","1"],["1","0"]]
assert solution.maximalRectangle(matrix) == 1
matrix = [["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]
assert solution.maximalRectangle(matrix) == 9
