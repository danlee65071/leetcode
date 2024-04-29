from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        def solve(remainder_nums: List[int], cur_subset: List[int]) -> None:
            subsets.append(cur_subset[:])
            for i, num in enumerate(remainder_nums):
                if i == 0 or (i > 0 and num != remainder_nums[i-1]):
                    cur_subset.append(num)
                    solve(remainder_nums[i+1:], cur_subset)
                    cur_subset.pop()

        solve(nums, [])
        return subsets


solution = Solution()
nums = [1,2,2]
assert solution.subsetsWithDup(nums) == [[],[1],[1,2],[1,2,2],[2],[2,2]]
nums = [0]
assert solution.subsetsWithDup(nums) == [[],[0]]

