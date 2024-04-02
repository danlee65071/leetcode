from typing import List


class Solution:
    def find_min_ptr(self, nums: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(nums) - 1
        min_ptr = tmp_ptr = (left_ptr + right_ptr) // 2
        if nums[left_ptr] <= nums[min_ptr] <= nums[right_ptr]:
            return left_ptr
        elif nums[left_ptr] >= nums[min_ptr] >= nums[right_ptr]:
            return right_ptr
        while right_ptr - 1 > left_ptr:
            if nums[tmp_ptr] > nums[left_ptr]:
                left_ptr = tmp_ptr
            elif nums[tmp_ptr] < nums[right_ptr]:
                right_ptr = tmp_ptr
            tmp_ptr = (left_ptr + right_ptr) // 2
            if nums[tmp_ptr] < nums[min_ptr]:
                min_ptr = tmp_ptr
        if nums[left_ptr] < nums[min_ptr]:
            min_ptr = left_ptr
        elif nums[right_ptr] < nums[min_ptr]:
            min_ptr = right_ptr
        return min_ptr

    def search(self, nums: List[int], target: int) -> int:
        min_ptr = self.find_min_ptr(nums)
        left_ptr = min_ptr
        rigth_ptr = len(nums) - 1
        if target > nums[-1]:
            left_ptr = 0
            rigth_ptr = min_ptr
        if nums[left_ptr] == target:
            return left_ptr
        elif nums[rigth_ptr] == target:
            return rigth_ptr
        target_ptr = (left_ptr + rigth_ptr) // 2
        while rigth_ptr - 1 > left_ptr:
            if nums[target_ptr] == target:
                return target_ptr
            elif nums[target_ptr] > target:
                rigth_ptr = target_ptr
            else:
                left_ptr = target_ptr
            target_ptr = (left_ptr + rigth_ptr) // 2
        return target_ptr if nums[target_ptr] == target else -1


solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))
nums = [4,5,6,7,0,1,2]
target = 3
print(solution.search(nums, target))
nums = [1]
target = 0
print(solution.search(nums, target))   
nums = [1]
target = 1
print(solution.search(nums, target))
nums = [1,3]
target = 2
print(solution.search(nums, target))
nums = [1,3]
target = 3
print(solution.search(nums, target))
nums = [1,3]
target = 1
print(solution.search(nums, target))
nums = [1,3,5]
target = 3
print(solution.search(nums, target))
nums = [3,5,1]
target = 5
print(solution.search(nums, target))
nums = [2,3,4,5,6,7,8,9,1]
target = 9
print(solution.search(nums, target))
nums = [6,7,1,2,3,4,5]
target = 7
print(solution.search(nums, target))
