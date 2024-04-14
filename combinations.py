from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def solve(cur_combination: List[int], start: int) -> None:
            if len(cur_combination) == k:
                combinations.append(cur_combination[:])
                return
            for num in range(start, n+1):
                cur_combination.append(num)
                solve(cur_combination, num+1)
                cur_combination.pop()

        solve([], 1)
        return combinations


solution = Solution()
n = 4
k = 2
assert solution.combine(n, k) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
n = 1
k = 1
assert solution.combine(n, k) == [[1]]
