from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left, right = 0, len(nums) - 1
        indexes = []
        while right - 1 > left:
            mid = (left + right) // 2
            if nums[mid] == target:
                l_target = r_target = mid
                while l_target - 1 >= 0:
                    if nums[l_target - 1] == target:
                        l_target -= 1
                    else:
                        break
                while r_target + 1 < len(nums):
                    if nums[r_target + 1] == target:
                        r_target += 1
                    else:
                        break
                indexes = [l_target, r_target]
                if len(indexes) == 1:
                    indexes = indexes * 2
                return indexes
            elif nums[mid] < target:
                left = mid
            else:
                right = mid
        if nums[left] == target:
            indexes.append(left)
        if nums[right] == target and right != left:
            indexes.append(right)
        if len(indexes) == 1:
            indexes = indexes * 2
        return indexes if indexes else [-1, -1]


solution = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(solution.searchRange(nums, target))
nums = [5,7,7,7,8,10]
target = 7
print(solution.searchRange(nums, target))
nums = [5,7,7,7,8,10]
target = 6
print(solution.searchRange(nums, target))
nums = []
target = 6
print(solution.searchRange(nums, target))
nums = [6]
target = 6
print(solution.searchRange(nums, target))
nums = [1,3]
target = 1
print(solution.searchRange(nums, target))
nums = [1,2,2]
target = 2
print(solution.searchRange(nums, target))
nums = [1,1,2]
target = 1
print(solution.searchRange(nums, target))
nums = [1,2,3]
target = 2
print(solution.searchRange(nums, target))
