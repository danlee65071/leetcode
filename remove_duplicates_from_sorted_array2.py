from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        repeats = 1
        for right in range(1, len(nums)):
            if nums[right-1] != nums[right]:
                repeats = 1
            else:
                repeats += 1
            if repeats <= 2:
                nums[left] = nums[right]
                left += 1
        return left


solution = Solution()
nums = [1,1,1,2,2,3]
assert solution.removeDuplicates(nums) == 5
assert nums[:5] == [1,1,2,2,3]
nums = [0,0,1,1,1,1,2,3,3]
assert solution.removeDuplicates(nums) == 7
assert nums[:7] == [0,0,1,1,2,3,3]
