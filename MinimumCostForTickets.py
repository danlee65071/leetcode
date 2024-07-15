from typing import List
from functools import lru_cache


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # top-down
        @lru_cache(None)
        def dp(i, rem_days):
            if i >= len(days):
                return 0
            if rem_days - days[i] >= 0:
                return dp(i + 1, rem_days)
            return min(
                dp(i + 1, days[i]) + costs[0],
                dp(i + 1, days[i] + 6) + costs[1],
                dp(i + 1, days[i] + 29) + costs[2],
            )

        return dp(0, 0)


solution = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
assert solution.mincostTickets(days, costs) == 11
days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
costs = [2, 7, 15]
assert solution.mincostTickets(days, costs) == 17
days = [1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28]
costs = [3, 13, 45]
assert solution.mincostTickets(days, costs) == 44
