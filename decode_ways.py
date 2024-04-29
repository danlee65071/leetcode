class Solution:
    def numDecodings(self, s: str) -> int:
        map_s = dict()

        def solve(cur_s: str, remain_s: str) -> int:
            if cur_s and cur_s[0] == '0':
                return 0
            if not remain_s:
                return 1
            if map_s.get(remain_s) is not None:
                return map_s.get(remain_s)
            map_s[remain_s] = map_s.get(remain_s, 0) + solve(remain_s[0], remain_s[1:])
            if len(remain_s) >= 2 and int(remain_s[:2]) <= 26:
                map_s[remain_s] = map_s.get(remain_s, 0) + solve(remain_s[:2], remain_s[2:])
            return map_s[remain_s]

        solve('', s)
        return map_s.get(s, 0)


solution = Solution()
s = "226"
assert solution.numDecodings(s) == 3
s = "12"
assert solution.numDecodings(s) == 2
s = "06"
assert solution.numDecodings(s) == 0
s = "27"
assert solution.numDecodings(s) == 1
