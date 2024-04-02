from typing import List


class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    #     parenthesis = [[] for _ in range(n+1)]
    #     parenthesis[0].append('')
    #     for i in range(n+1):
    #         for j in range(i):
    #             parenthesis[i] += ['(' + x + ')' + y for x in parenthesis[j] for y in parenthesis[i - j - 1]]
    #     return parenthesis[-1]
    def generate(self, num_open, num_closed, parenthes, res):
        if num_closed == 0 and num_open == 0:
            res.append(parenthes)
            return
        if num_open > 0:
            self.generate(num_open-1, num_closed, parenthes+'(', res)
        if num_closed > 0 and num_closed > num_open:
            self.generate(num_open, num_closed-1, parenthes+')', res)

    def generateParenthesis(self, n: int) -> List[str]:
        num_open = n
        num_closed = n
        res = []
        self.generate(num_open, num_closed, '', res)
        return res


s = Solution()
print(s.generateParenthesis(3))
