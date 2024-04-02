from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        list_ranges = []
        first_num = nums[0]
        for it, num in enumerate(nums[1:]):
            if num != nums[it] + 1:
                tmp_str = f'{first_num}->{nums[it]}' if first_num != nums[it] else f'{first_num}'
                list_ranges.append(tmp_str)
                first_num = num
        tmp_str = f'{first_num}->{nums[-1]}' if first_num != nums[-1] else f'{first_num}'
        list_ranges.append(tmp_str)
        return list_ranges


s = Solution()
print(s.summaryRanges([0,1,2,4,5,7]))
print(s.summaryRanges([0]))
print(s.summaryRanges([0,2,3,4,6,8,9]))
print(s.summaryRanges([0,2,4,6,9]))
print(s.summaryRanges([]))
