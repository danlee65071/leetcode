from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for i in nums:
            rob1, rob2 = rob2, max(i+rob1, rob2)
        return rob2


solution = Solution()

