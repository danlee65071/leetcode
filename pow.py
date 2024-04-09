class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0

        def _pow(x: float, n: int) -> float:
            if n == 0:
                return 1
            res = _pow(x, n//2)
            res *= res
            return x * res if n % 2 else res

        x_pow_n = _pow(x, abs(n))
        return x_pow_n if n > 0 else 1 / x_pow_n


solution = Solution()
x = 2.00000
n = 10
assert solution.myPow(x, n) == 1024.00000
x = 2.10000
n = 3
assert solution.myPow(x, n) == 9.26100
x = 2.00000
n = -2
assert solution.myPow(x, n) == 0.25
