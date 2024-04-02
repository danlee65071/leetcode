from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        next_num = 1
        for num in nums:
            if num == next_num:
                next_num += 1
        for num in nums[::-1]:
            if num == next_num:
                next_num += 1
        return next_num


solution = Solution()
nums = [1,2,0]
print(solution.firstMissingPositive(nums))
nums = [3,4,-1,1]
print(solution.firstMissingPositive(nums))
nums = [7,8,9,11,12]
print(solution.firstMissingPositive(nums))
nums = [1,2,6,3,5,4]
print(solution.firstMissingPositive(nums))
nums = [0,2,2,4,0,1,0,1,3]
print(solution.firstMissingPositive(nums))
