from typing import List


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        interleaving_matrix: List[List[bool]] = [[False] * (len(s2) + 1) for _ in range(len(s1)+1)]
        interleaving_matrix[len(s1)][len(s2)] = True
        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and interleaving_matrix[i+1][j]:
                    interleaving_matrix[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and interleaving_matrix[i][j+1]:
                    interleaving_matrix[i][j] = True
        return interleaving_matrix[0][0]


solution: Solution = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
assert solution.isInterleave(s1, s2, s3) == True
