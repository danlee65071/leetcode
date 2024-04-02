from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for it in range(1, numRows):
            layer = [1]
            if it > 1:
                layer += [res[-1][i-1] + res[-1][i] for i in range(1, len(res[-1]))]
            layer.append(1)
            res.append(layer)
        return res


s = Solution()
numRows = 5
print(s.generate(numRows))
numRows = 1
print(s.generate(numRows))
numRows = 2
print(s.generate(numRows))

