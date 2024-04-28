class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        scramble_map = dict()

        def solve(s1: str, s2: str) -> bool:
            if len(s1) == 1:
                return s1 == s2
            elif s1 == s2:
                return True
            key = s1 + s2
            if scramble_map.get(key) is not None:
                return scramble_map[key]
            for i in range(1, len(s1)):
                if (solve(s1[:i], s2[:i]) and solve(s1[i:], s2[i:])) or \
                        (solve(s1[:i], s2[len(s1)-i:]) and solve(s1[i:], s2[:len(s1)-i])):
                    scramble_map[key] = True
                    return True
            scramble_map[key] = False
            return False

        return solve(s1, s2)


solution = Solution()
s1 = "great"
s2 = "rgeat"
assert solution.isScramble(s1, s2) == True
s1 = "a"
s2 = "a"
assert solution.isScramble(s1, s2) == True
s1 = "abcde"
s2 = "caebd"
assert solution.isScramble(s1, s2) == False
s1 = "abb"
s2 = "bba"
assert solution.isScramble(s1, s2) == True
