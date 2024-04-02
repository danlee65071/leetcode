from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
                k += 1
        return k
                