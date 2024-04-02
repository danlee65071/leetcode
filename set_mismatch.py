from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_dict = {i+1: 0 for i in range(len(nums))}
        for num in nums:
            nums_dict[num] += 1
        repeated_num, empty_num = 0, 0
        for key, val in nums_dict.items():
            if val == 0:
                empty_num = key
            elif val > 1:
                repeated_num = key
        return repeated_num, empty_num


s = Solution()
tests = [
    [1, 2, 2, 4],
    [1, 1],
    [3, 2, 3, 4, 6, 5],
    [3, 2, 2]
]
for idx, test in enumerate(tests):
    print(f'Test: {idx}')
    print(f'\tInput: {test}')
    print(f'\tOutput: {s.findErrorNums(test)}')
