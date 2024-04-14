class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        map_s, map_t = dict(), dict()
        s_have, t_have = 0, len(t)
        res = [-1, -1]
        res_len = float('inf')
        left = 0
        for c in t:
            map_t[c] = map_t.get(c, 0) + 1
        for right in range(len(s)):
            if map_t.get(s[right]) is not None:
                map_s[s[right]] = map_s.get(s[right], 0) + 1
                if map_t[s[right]] >= map_s[s[right]]:
                    s_have += 1
            while s_have == t_have:
                cur_len = right - left + 1
                if cur_len < res_len:
                    res = [left, right]
                    res_len = cur_len
                if map_s.get(s[left]) is not None:
                    map_s[s[left]] -= 1
                    if map_s[s[left]] < map_t[s[left]]:
                        s_have -= 1
                left += 1
        return s[res[0]: res[-1] + 1] if res_len != float('inf') else ''


solution = Solution()
s = "ADOBECODEBANC"
t = "ABC"
assert solution.minWindow(s, t) == "BANC"
s = "a"
t = "a"
assert solution.minWindow(s, t) == "a"
s = "a"
t = "aa"
assert solution.minWindow(s, t) == ""
s = "aa"
t = "aa"
assert solution.minWindow(s, t) == "aa"
