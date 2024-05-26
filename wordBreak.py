from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # bottom-up
        dp: List[bool] = [False] * len(s)
        for i in range(len(dp)):
            for word in wordDict:
                if i >= len(word) - 1 and (i == len(word) - 1 or dp[i - len(word)] == True):
                    if s[i - len(word) + 1: i + 1] == word:
                        dp[i] = True
                        break
        return dp[-1]


solution: Solution = Solution()
s: str = "leetcode"
wordDict: str = ["leet", "code"]
assert solution.wordBreak(s, wordDict) == True
s: str = "applepenapple"
wordDict: str = ["apple", "pen"]
assert solution.wordBreak(s, wordDict) == True
s: str = "catsandog"
wordDict: str = ["cats", "dog", "sand", "and", "cat"]
assert solution.wordBreak(s, wordDict) == False
