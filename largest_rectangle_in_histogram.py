from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List = []
        max_area: int = 0
        for pos, height in enumerate(heights):
            if pos == 0 or height >= stack[-1][1]:
                stack.append([pos, height])
            else:
                while stack and height < stack[-1][1]:
                    prev_pos, prev_height = stack.pop()
                    max_area = max(max_area, prev_height * (pos - prev_pos))
                stack.append([prev_pos, height])
        for (pos, height) in stack:
            max_area = max(max_area, height * (len(heights) - pos))
        return max_area


solution = Solution()
heights = [2,1,5,6,2,3]
assert solution.largestRectangleArea(heights) == 10
heights = [2,4]
assert solution.largestRectangleArea(heights) == 4
