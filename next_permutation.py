from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return
        first_pointer = len(nums) - 1
        while first_pointer > 0:
            if nums[first_pointer] <= nums[first_pointer-1]:
                first_pointer -= 1
            else:
                break
        if first_pointer == 0:
            nums[:] = nums[::-1]
            return
        first_pointer = first_pointer - 1
        second_pointer = len(nums) - 1
        while nums[second_pointer] <= nums[first_pointer]:
            second_pointer -= 1
        nums[first_pointer], nums[second_pointer] = nums[second_pointer], nums[first_pointer]
        for it in range((len(nums) - first_pointer - 1) // 2):
            nums[first_pointer + 1 + it], nums[len(nums) - it - 1] = nums[len(nums) - it - 1], nums[first_pointer + 1 + it] 


s = Solution()
nums = [3,2,1]
s.nextPermutation(nums)
print(nums)
nums = [1,2,3]
s.nextPermutation(nums)
print(nums)
nums = [1,1,5]
s.nextPermutation(nums)
print(nums)
nums = [1,3,2,4]
s.nextPermutation(nums)
print(nums)
nums = [1,3,2]
s.nextPermutation(nums)
print(nums)
nums = [2,3,1]
s.nextPermutation(nums)
print(nums)
nums = [1,5,1]
s.nextPermutation(nums)
print(nums)
nums = [1,1]
s.nextPermutation(nums)
print(nums)
