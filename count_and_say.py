class Solution:
    def countAndSay(self, n: int) -> str:
        res = ['1']
        for _ in range(1, n):
            prev = res[-1]
            cur_say = []
            cur_d, count = prev[0], 0
            for d in prev:
                if cur_d == d:
                    count += 1
                else:
                    cur_say += [str(count), cur_d]
                    cur_d = d
                    count = 1
            if count:
                cur_say += [str(count), d]
            res.append(''.join(cur_say))
        return res[-1]


s = Solution()
print(s.countAndSay(4))
