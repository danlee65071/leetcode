from typing import List


class Solution:
    def check_left_direction(self, left_sum, right_sum,
                             nums, pivot_index):
        for index in range(pivot_index, 0, -1):
            left_sum -= nums[index]
            right_sum += nums[index+1]
            if left_sum == right_sum:
                return index
        if sum(nums[1:]) == 0:
            return 0
        return -1

    def check_right_direction(self, left_sum, right_sum,
                              nums, pivot_index):
        for index in range(pivot_index, len(nums)-1):
            left_sum += nums[index-1]
            right_sum -= nums[index]
            if left_sum == right_sum:
                return index
        if sum(nums[:-1]) == 0:
            return len(nums) - 1
        return -1

    def pivotIndex(self, nums: List[int]) -> int:
        pivot_index = 0 if len(nums) // 2 - 1 <= 0 else len(nums) // 2 - 1
        left_sum = sum(nums[:pivot_index])
        right_sum = sum(nums[pivot_index+1:])
        if left_sum == right_sum:
            return pivot_index
        left_pivot = self.check_left_direction(left_sum, right_sum, nums,
                                               pivot_index-1)
        if left_pivot > -1:
            pivot_index = left_pivot
        else:
            right_pivot = self.check_right_direction(left_sum, right_sum,
                                                     nums, pivot_index+1)
            if right_pivot > -1:
                pivot_index = right_pivot
            else:
                pivot_index = -1
        return pivot_index


s = Solution()
print(s.pivotIndex([1,7,3,6,5,6]))
print(s.pivotIndex([1,2,3]))
print(s.pivotIndex([2,1,-1]))
print(s.pivotIndex([-1,-1,-1,-1,-1,0]))
print(s.pivotIndex([-1,-1,-1,0,-1,-1]))
print(s.pivotIndex([-1,-1,-1,0,-1,0]))
print(s.pivotIndex([-1,-1,-1,0,1,1]))
print(s.pivotIndex([-1,-1,0,0,-1,-1]))
print(s.pivotIndex([0]))
print(s.pivotIndex([-1,-1,1,-1,-1,0]))
