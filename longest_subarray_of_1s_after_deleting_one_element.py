from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest_sub = tmp_sub = 0
        is_use_zero = False
        zero_ind = -1
        zero_count = 0
        it = 0
        while it < len(nums):
            if nums[it] == 1:
                tmp_sub += 1
            elif nums[it] == 0 and is_use_zero is False:
                is_use_zero = True
                zero_ind = it
                zero_count += 1
            else:
                if tmp_sub > longest_sub:
                    longest_sub = tmp_sub
                tmp_sub = 0
                is_use_zero = False
                it = zero_ind
                zero_count += 1
            it += 1
        if tmp_sub != 0:
            if tmp_sub > longest_sub:
                longest_sub = tmp_sub
        if zero_count == 0:
            longest_sub -= 1
        return longest_sub


s = Solution()
print(s.longestSubarray([1, 1, 0, 1]))
print(s.longestSubarray([0, 1, 1, 1, 0, 1, 1, 0, 1]))
print(s.longestSubarray([1, 1, 1]))
