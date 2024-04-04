class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str_to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
                      '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        int_to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                      5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
        
        def atoi(num: str):
            res = 0
            for it, c in enumerate(num[::-1]):
                res += str_to_int[c] * pow(10, it)
            return res

        def itoa(num: int):
            if num == 0:
                return '0'
            res = []
            while num:
                res.append(int_to_str[num % 10])
                num //= 10
            return ''.join(res[::-1])

        n1, n2 = atoi(num1), atoi(num2)
        return itoa(n1 * n2)


solution = Solution()
num1 = "2"
num2 = "3"
assert solution.multiply(num1, num2) == '6'
num1 = "123"
num2 = "456"
assert solution.multiply(num1, num2) == '56088'
num1 = "0"
num2 = "456"
assert solution.multiply(num1, num2) == '0'
