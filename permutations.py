from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []

        def solve(cur_permutation: List[int], remains: List[int]):
            if not remains:
                permutations.append(cur_permutation.copy())
                return
            for num in remains:
                cur_permutation.append(num)
                tmp_remains = [n for n in remains if n != num]
                solve(cur_permutation, tmp_remains)
                cur_permutation.pop()

        solve([], nums)
        return permutations


solution = Solution()
nums = [1,2,3]
assert solution.permute(nums) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
nums = [0,1]
assert solution.permute(nums) == [[0,1],[1,0]]
nums = [1]
assert solution.permute(nums) == [[1]]
