from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        num_zero_dups = 0
        len_ = len(arr) - 1
        for i, num in enumerate(arr):
            if i - len_ + num_zero_dups > 0:
                break
            if num == 0:
                if i == len_ - num_zero_dups:
                    arr[len_] = 0
                    len_ -= 1
                    break
                num_zero_dups += 1
        right = len_ - num_zero_dups
        for i in range(right, -1, -1):
            if arr[i] == 0:
                arr[i + num_zero_dups] = 0
                num_zero_dups -= 1
            arr[i + num_zero_dups] = arr[i]


solution = Solution()
arr = [1, 0, 2, 3, 0, 4, 5, 0]
solution.duplicateZeros(arr)
assert arr == [1, 0, 0, 2, 3, 0, 0, 4]
arr = [8, 4, 5, 0, 0, 0, 0, 7]
solution.duplicateZeros(arr)
assert arr == [8, 4, 5, 0, 0, 0, 0, 0]
