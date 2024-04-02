class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = dict()
        for c in s1:
            s1_map[c] = s1_map.get(c, 0) + 1
        s2_map = dict()
        for c in s2[:len(s1)]:
            s2_map[c] = s2_map.get(c, 0) + 1
        i, s1_len = 0, len(s1)
        while i + s1_len < len(s2):
            matches = 0
            for c in s1:
                if c in s2_map.keys() and s1_map[c] == s2_map[c]:
                    matches += 1
            if matches == len(s1):
                return True
            s2_map[s2[i]] = s2_map.get(s2[i], 1) - 1
            s2_map[s2[i + s1_len]] = s2_map.get(s2[i + s1_len], 0) + 1
            i += 1
        matches = 0
        for c in s1:
            if c in s2_map.keys() and s1_map[c] == s2_map[c]:
                matches += 1
        if matches == len(s1):
            return True
        return False


s = Solution()
print('Test1')
s1 = 'ab'
s2 = 'eidbaooo'
print(s.checkInclusion(s1, s2))
print('Test2')
s1 = 'ab'
s2 = 'eidboaoo'
print(s.checkInclusion(s1, s2))
print('Test3')
s1 = 'eidboaoo'
s2 = 'a'
print(s.checkInclusion(s1, s2))
print('Test4')
s1 = 'adc'
s2 = 'dcda'
print(s.checkInclusion(s1, s2))
