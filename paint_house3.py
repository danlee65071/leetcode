from typing import List


class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        # top-down
        max_cost = 10 ** 4 + 1
        memo = dict()

        def dp(i, prev_color, num_neighborhoods):
            if i == m:
                return 0 if num_neighborhoods == target else max_cost
            if num_neighborhoods > target:
                return max_cost

            if memo.get((i, prev_color, num_neighborhoods)) is not None:
                return memo[(i, prev_color, num_neighborhoods)]

            min_cost = max_cost
            if houses[i] != 0:
                neighborhood = 0 if prev_color == houses[i] else 1
                min_cost = dp(i+1, houses[i], num_neighborhoods + neighborhood)
            else:
                for color in range(1, n+1):
                    neighborhood = 0 if prev_color == color else 1
                    cur_cost = dp(i+1, color, num_neighborhoods + neighborhood) + cost[i][color-1]
                    min_cost = min(min_cost, cur_cost)
            memo[(i, prev_color, num_neighborhoods)] = min_cost
            return memo[(i, prev_color, num_neighborhoods)]

        min_cost = dp(0, 0, 0)
        return min_cost if min_cost != max_cost else -1


solution = Solution()
houses = [0, 0, 0, 0, 0]
cost = [[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
m = 5
n = 2
target = 3
assert solution.minCost(houses, cost, m, n, target) == 9
