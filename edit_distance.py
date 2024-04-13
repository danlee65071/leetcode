class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        words_matrix = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]
        for i in range(len(word2) + 1):
            words_matrix[i][-1] = len(word2) - i
        for j in range(len(word1) + 1):
            words_matrix[-1][j] = len(word1) - j
        for i in range(len(word2) - 1, -1, -1):
            for j in range(len(word1) - 1, -1, -1):
                if word2[i] == word1[j]:
                    words_matrix[i][j] = words_matrix[i+1][j+1]
                else:
                    words_matrix[i][j] = 1 + min(words_matrix[i+1][j+1],
                                                 words_matrix[i+1][j],
                                                 words_matrix[i][j+1])
        return words_matrix[0][0]


solution = Solution()
word1 = "horse"
word2 = "ros"
assert solution.minDistance(word1, word2) == 3
word1 = "intention"
word2 = "execution"
assert solution.minDistance(word1, word2) == 5
