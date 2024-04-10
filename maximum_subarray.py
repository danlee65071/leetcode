from typing import List


class Solution:
    # algorithm Kadane
    def maxSubArray(self, nums: List[int]) -> int:
        max_end, total_max = nums[0], nums[0]
        for num in nums[1:]:
            max_end = max(max_end+num, num)
            total_max = max(total_max, max_end)
        return total_max


solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
assert solution.maxSubArray(nums) == 6
nums = [1]
assert solution.maxSubArray(nums) == 1
nums = [5,4,-1,7,8]
assert solution.maxSubArray(nums) == 23
