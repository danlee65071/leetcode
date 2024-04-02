class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ngram_set = set()
        start, end = 0, len(needle)
        while end <= len(haystack):
            ngram_set.add(haystack[start: end])
            if needle in ngram_set:
                return start
            start += 1
            end += 1
        return -1


s = Solution()
print(s.strStr('sadbutsad', 'sad'))
print(s.strStr('butsad', 'sad'))
print(s.strStr('leetcode', 'leeto'))
print(s.strStr('sad', 'sad'))
print(s.strStr('sad', 'sadbutsad'))
