from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        max_pos, prev_max_pos = 1, 0
        for it, num in enumerate(nums):
            if num > nums[max_pos]:
                prev_max_pos = max_pos
                max_pos = it
            elif num > nums[prev_max_pos] and num < nums[max_pos]:
                prev_max_pos = it
        return max_pos if nums[prev_max_pos] == 0 or nums[max_pos] / nums[prev_max_pos] >= 2 else -1
