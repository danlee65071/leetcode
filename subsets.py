from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def solve(cur_subset: List[int], remainder_nums: List[int]) -> None:
            res.append(cur_subset[:])
            for i, num in enumerate(remainder_nums):
                cur_subset.append(num)
                new_remainder_nums = remainder_nums[i+1:]
                solve(cur_subset, new_remainder_nums)
                cur_subset.pop()

        solve([], nums)
        return res


solution = Solution()
nums = [1,2,3]
assert sorted(solution.subsets(nums)) == sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
nums = [0]
assert solution.subsets(nums) == [[],[0]]
