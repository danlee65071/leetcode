from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(len(nums)):
            if abs(nums[i]) > 0 and abs(nums[i]) - 1 < len(nums) and \
                    abs(nums[i]) - 1 >= 0 and nums[abs(nums[i]) - 1] >= 0:
                nums[abs(nums[i]) - 1] = -1 * nums[abs(nums[i]) - 1] if abs(nums[abs(nums[i]) - 1]) > 0 else -1 * (len(nums) + 1)
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1


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
nums = [3,4,0,2]
print(solution.firstMissingPositive(nums))
nums = [3,3,1,4,0]
print(solution.firstMissingPositive(nums))
nums = [1, 1]
print(solution.firstMissingPositive(nums))
