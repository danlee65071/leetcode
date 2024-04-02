from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        map_words = dict()
        for word in words:
            map_words[word] = map_words.get(word, 0) + 1
        indexies = []
        it = 0
        while it + len(words[0]) * len(words) <= len(s):
            tmp_map = dict()
            matches = 0
            num_subwords = 0
            while num_subwords < len(words):
                sub_word = s[it + num_subwords * len(words[0]): it + (num_subwords + 1) * len(words[0])]
                tmp_map[sub_word] = tmp_map.get(sub_word, 0) + 1
                if sub_word in map_words.keys() and tmp_map[sub_word] <= map_words[sub_word]:
                    matches += 1
                num_subwords += 1

            if matches == len(words):
                indexies.append(it)
            it += 1
        return indexies


solution = Solution()
s = "barfoothefoobarman"
words = ["foo", "bar"]
print(solution.findSubstring(s, words))
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(solution.findSubstring(s, words))
s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(solution.findSubstring(s, words))
s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
print(solution.findSubstring(s, words))
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
print(solution.findSubstring(s, words))
