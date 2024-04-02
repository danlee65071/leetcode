from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in map_anagrams.keys():
                map_anagrams[sorted_s] = [s]
            else:
                map_anagrams[sorted_s].append(s)
        return map_anagrams.values()
