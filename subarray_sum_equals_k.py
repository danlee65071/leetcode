from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_map = {0: 1}
        counter = 0
        for num in nums:
            prefix_sum += num
            counter += prefix_map.get(prefix_sum - k, 0)
            prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
        return counter


s = Solution()
print(s.subarraySum([1,1,1], 2))
print(s.subarraySum([1,2,3], 3))
