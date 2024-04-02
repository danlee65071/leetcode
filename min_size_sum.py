from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, res = 0, len(nums) + 1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                res = min(res, j - i + 1)
                target += nums[i]
                i += 1
        return res % (len(nums) + 1)
    # def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        


s = Solution()
print(s.minSubArrayLen(7, [2,3,4,2,3,1]))
print(s.minSubArrayLen(4, [1,4,4]))
print(s.minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(s.minSubArrayLen(11, [1,2,3,4,5]))
print(s.minSubArrayLen(7, [1,4,1,2,2,4,3]))
