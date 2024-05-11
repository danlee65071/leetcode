from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums_and_points = dict()
        max_num = 0
        for n in nums:
            if n > max_num:
                max_num = n
            nums_and_points[n] = nums_and_points.get(n, 0) + n
        memo = dict()

        def dp(i):
            if i == 0:
                return 0
            if i == 1:
                return nums_and_points.get(1, 0)
            if memo.get(i) is None:
                memo[i] = max(dp(i-1), dp(i-2) + nums_and_points.get(i, 0))
            return memo[i]

        return dp(max_num)


solution = Solution()
nums = [2,2,3,3,3,4]
assert solution.deleteAndEarn(nums) == 9
