from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def solve(cur_permutation: List[int], remains: List[int]):
            if not remains:
                permutations.append(cur_permutation.copy())
                return
            prev = None
            remains = sorted(remains)
            for it, num in enumerate(remains):
                if prev is not None and num == prev:
                    continue
                cur_permutation.append(num)
                tmp_remains = [n for i, n in enumerate(remains) if i != it]
                solve(cur_permutation, tmp_remains)
                cur_permutation.pop()
                prev = num

        solve([], nums)
        return permutations


solution = Solution()
nums = [1,1,2]
assert solution.permuteUnique(nums) == [[1,1,2], [1,2,1], [2,1,1]]
nums = [1,2,3]
assert solution.permuteUnique(nums) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
