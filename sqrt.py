class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, max(1, x // 2)
        cur = (right + left) // 2
        while left <= right:
            if cur * cur == x:
                return cur
            elif cur * cur < x:
                left = cur + 1
            else:
                right = cur - 1
            cur = (right + left) // 2
        return cur


solution = Solution()
x = 4
assert solution.mySqrt(x) == 2
x = 8
assert solution.mySqrt(x) == 2
x = 17
assert solution.mySqrt(x) == 4
x = 1
assert solution.mySqrt(x) == 1
x = 0
assert solution.mySqrt(x) == 0
