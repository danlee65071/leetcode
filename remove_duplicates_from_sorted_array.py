from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums = set(nums)
        nums[:] = sorted(set_nums)
        return len(set_nums)


s = Solution()
# test1
nums = [1, 1, 2]
print(s.removeDuplicates(nums))
print(nums)
# test2
nums = [-1, 0, 0, 0, 0, 3, 3]
print(s.removeDuplicates(nums))
print(nums)
