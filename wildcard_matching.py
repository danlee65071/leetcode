class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        table = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        s_list = [''] + list(s)
        p_list = [''] + list(p)
        table[0][0] = True
        for s_ptr in range(len(s_list)):
            for p_ptr in range(len(p_list)):
                if p_list[p_ptr] == s_list[s_ptr] or (p_list[p_ptr] == '?' and s_list[s_ptr]):
                    table[s_ptr][p_ptr] = True if table[max(s_ptr - 1, 0)][max(p_ptr - 1, 0)] else False
                elif p_list[p_ptr] == '*':
                    table[s_ptr][p_ptr] = True if table[s_ptr][max(p_ptr - 1, 0)] or \
                        table[max(s_ptr - 1, 0)][p_ptr] else False
        return table[-1][-1]


solution = Solution()
s = "aa"
p = "a"
assert solution.isMatch(s, p) == False
s = "aa"
p = "*"
assert solution.isMatch(s, p) == True
s = "aa"
p = "*a"
assert solution.isMatch(s, p) == True
s = "aa"
p = "?a"
assert solution.isMatch(s, p) == True
s = "cb"
p = "?a"
assert solution.isMatch(s, p) == False
s = "cb"
p = "*a"
assert solution.isMatch(s, p) == False
s = "a"
p = "*a"
assert solution.isMatch(s, p) == True
s = "adceb"
p = "*a*b"
assert solution.isMatch(s, p) == True
s = ""
p = "******"
assert solution.isMatch(s, p) == True
s = "abcabczzzde"
p = "*abc???de*"
assert solution.isMatch(s, p) == True
s = ""
p = "?"
assert solution.isMatch(s, p) == False
