from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp_nums = [num for num in nums if num != 0]
        tmp_nums += [0 for _ in range(len(nums) - len(tmp_nums))]
        nums[:] = tmp_nums
        