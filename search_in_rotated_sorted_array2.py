from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] > nums[mid]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] < nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                left += 1
        return False


solution = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
assert solution.search(nums, target) == True
nums = [2,5,6,0,0,1,2]
target = 3
assert solution.search(nums, target) == False
nums = [1,0,1,1,1]
target = 0
assert solution.search(nums, target) == True
