class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a = len(a)
        len_b = len(b)
        max_len = len_a
        remainder = 0
        res_str = ''
        
        if len_a > len_b:
            b = ''.join(['0' for _ in range(len_a - len_b)]) + b
        elif len_a < len_b:
            max_len = len_b
            a = ''.join(['0' for _ in range(len_b - len_a)]) + a

        for i in range(max_len):
            sum_ = int(a[max_len - 1 - i]) + int(b[max_len - 1 - i])
            if remainder == 0:
                if sum_ == 2 or sum_ == 0:
                    res_str += '0'
                    if sum_ == 2:
                        remainder += 1
                else:
                    res_str += '1'
            else:
                if sum_ == 2 or sum_ == 0:
                    res_str += '1'
                    if sum_ == 0:
                        remainder -= 1
                elif sum_ == 1:
                    res_str += '0'
        for r in range(remainder):
            if r == 0:
                res_str += '1'
        res_str = res_str[::-1]
        return res_str


s = Solution()
print(s.addBinary('100', '110010'))
