from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


solution = Solution()
nums = [1,3,5,6]
target = 2
print(solution.searchInsert(nums, target))
nums = [1,3,5,6]
target = 0
print(solution.searchInsert(nums, target))
nums = [1,3,5,6]
target = 7
print(solution.searchInsert(nums, target))
nums = []
target = 7
print(solution.searchInsert(nums, target))
nums = [1,3]
target = 1
print(solution.searchInsert(nums, target))
nums = [1,3]
target = 3
print(solution.searchInsert(nums, target))
nums = [1,3,5]
target = 1
print(solution.searchInsert(nums, target))
nums = [1,3,5]
target = 5
print(solution.searchInsert(nums, target))
nums = [1,3,5]
target = 3
print(solution.searchInsert(nums, target))
