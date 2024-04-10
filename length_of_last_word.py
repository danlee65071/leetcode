class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])


solution = Solution()
s = "Hello World"
assert solution.lengthOfLastWord(s) == 5
s = "   fly me   to   the moon  "
assert solution.lengthOfLastWord(s) == 4
