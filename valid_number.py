class Solution:
    def isNumber(self, s: str) -> bool:
        len_s = len(s)
        it = 0
        if s[it] == '+' or s[it] == '-':
            it += 1
        elif not s[it].isdigit() and s[it] != '.':
            return False
        while it < len_s and s[it].isdigit():
            it += 1
        if it >= len_s:
            if s[it-1].isdigit() or (s[it-1] == '.' and len_s > 1 and s[it-2].isdigit()):
                return True
            return False
        elif s[it] == '.':
            it += 1
            while it < len_s and s[it].isdigit() and s[it].lower() != 'e':
                it += 1
            if it == len_s:
                if s[it-1].isdigit() or (len_s > 1 and s[it-2].isdigit()):
                    return True
                return False
            if s[it] == 'e':
                if not s[it-1].isdigit() and (it-2 < 0 or not s[it-2].isdigit()): return False
                it += 1
                if it == len_s: return False
            if s[it-1] == 'e' and (s[it] == '+' or s[it] == '-'):
                it += 1
            elif not s[it].isdigit():
                return False
            while it < len_s and s[it].isdigit():
                it += 1
            if it == len_s:
                return True
        elif s[it].lower() == 'e':
            if not s[it-1].isdigit(): return False
            it += 1
            if it == len_s:
                if s[it-1].isdigit():
                    return True
                return False
            if s[it] == '+' or s[it] == '-':
                it += 1
            elif not s[it].isdigit():
                return False
            while it < len_s and s[it].isdigit():
                it += 1
            if it == len_s:
                if s[it-1].isdigit() or (s[it-1] == '.' and len_s > 1 and s[it-2].isdigit()):
                    return True
                return False
            if not s[it].isdigit():
                return False
        else:
            return False
        return False


solution = Solution()
s = "0"
assert solution.isNumber(s) == True
s = "e"
assert solution.isNumber(s) == False
s = "."
assert solution.isNumber(s) == False
s = "0089"
assert solution.isNumber(s) == True
s = "+3.14"
assert solution.isNumber(s) == True
s = "-90E3"
assert solution.isNumber(s) == True
s = "3e+7"
assert solution.isNumber(s) == True
s = "-123.456e789"
assert solution.isNumber(s) == True
s = "3."
assert solution.isNumber(s) == True
s = "..2"
assert solution.isNumber(s) == False
s = "0e"
assert solution.isNumber(s) == False
s = ".e"
assert solution.isNumber(s) == False
s = ".8+"
assert solution.isNumber(s) == False
s = "+E3"
assert solution.isNumber(s) == False
s = ".e1"
assert solution.isNumber(s) == False
