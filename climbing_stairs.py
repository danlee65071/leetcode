class Solution:
    def climbStairs(self, n: int) -> int:
        num_map = {1: 1, 2: 2}

        def solve(cur):
            if cur <= 2 or num_map.get(cur) is not None:
                if n > 2:
                    num_map[n] = num_map.get(n, 0) + num_map[cur]
                return
            solve(cur-1)
            solve(cur-2)
            num_map[cur] = num_map[n]

        solve(n)
        return num_map[n]


solution = Solution()
n = 2
assert solution.climbStairs(n) == 2
n = 3
assert solution.climbStairs(n) == 3
n = 4
assert solution.climbStairs(n) == 5
n = 5
assert solution.climbStairs(n) == 8
