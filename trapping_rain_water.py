from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left_ptr, left_ptr_max = 0, 0
        right_ptr, right_ptr_max = len(height) - 1, len(height) - 1
        water_square = 0
        while left_ptr < right_ptr:
            if height[left_ptr] <= height[right_ptr]:
                left_ptr += 1
                cur_water_square = height[left_ptr_max] - height[left_ptr]
                if height[left_ptr_max] < height[left_ptr]:
                    left_ptr_max = left_ptr
            else:
                right_ptr -= 1
                cur_water_square = height[right_ptr_max] - height[right_ptr]
                if height[right_ptr_max] < height[right_ptr]:
                    right_ptr_max = right_ptr
            water_square += cur_water_square if cur_water_square > 0 else 0
        return water_square


solution = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
assert solution.trap(height) == 6
height = [4,2,0,3,2,5]
assert solution.trap(height) == 9
