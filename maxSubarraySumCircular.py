from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum = float('-inf'), float('inf')
        cur_max, cur_min = 0, 0
        total = 0
        for num in nums:
            cur_max = max(cur_max + num, num)
            max_sum = max(cur_max, max_sum)
            cur_min = min(cur_min + num, num)
            min_sum = min(cur_min, min_sum)
            total += num
        return max_sum if total == min_sum else max(max_sum, total - min_sum)


solution = Solution()
nums = [1, -2, 3, -2]
assert solution.maxSubarraySumCircular(nums) == 3
