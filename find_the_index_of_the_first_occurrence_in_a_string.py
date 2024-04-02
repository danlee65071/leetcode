class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


s = Solution()
print(s.strStr("hello", "ll"))
print(s.strStr("a", "a"))