from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = []
        remain = 1
        for digit in digits[::-1]:
            if digit + remain == 10:
                res.append(0)
                remain = 1
            else:
                res.append(digit + remain)
                remain = 0
        if remain != 0:
            res.append(1)
        return res[::-1]
