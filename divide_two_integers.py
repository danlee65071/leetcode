class Solution:
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            curr_divisor, num_divisors = divisor, 1
            while dividend >= curr_divisor:
                dividend -= curr_divisor
                res += num_divisors
                curr_divisor = curr_divisor << 3
                num_divisors = num_divisors << 3
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))
print(s.divide(-10, 3))
print(s.divide(-10, -3))
print(s.divide(10, 1))
print(s.divide(-2147483648, -2))
