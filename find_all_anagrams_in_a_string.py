from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        map_p = dict()
        for c in p:
            map_p[c] = map_p.get(c, 0) + 1
        map_s = dict()
        anagrams_ids = []
        i = 0
        while i < len(s):
            map_s[s[i]] = map_s.get(s[i], 0) + 1
            if i >= len(p):
                map_s[s[i - len(p)]] -= 1
            matches = 0
            for k, v in map_p.items():
                if map_s.get(k, 0) == v:
                    matches += v
            if matches == len(p):
                anagrams_ids.append(i+1-len(p))
            i += 1
        return anagrams_ids


solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p))
s = "abab"
p = "ab"
print(solution.findAnagrams(s, p))
