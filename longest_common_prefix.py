from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = []
        is_finished = False
        it = 0
        while not is_finished:
            if it >= len(strs[0]):
                break
            cur_char = strs[0][it]
            for word in strs:
                if it >= len(word) or cur_char != word[it]:
                    is_finished = True
                    break
            if not is_finished:
                longest_prefix.append(cur_char)
            it += 1
        return ''.join(longest_prefix)


s = Solution()
print(s.longestCommonPrefix(["flower","flow","flight"]))
print(s.longestCommonPrefix(["dog","racecar","car"]))
