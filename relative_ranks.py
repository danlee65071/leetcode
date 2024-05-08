from typing import List, Tuple


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        scores_with_indexes: List[Tuple[int]] = [(s, i) for i, s in enumerate(score)]
        scores_with_indexes = sorted(scores_with_indexes, reverse=True)
        answer: List = [None] * len(score)
        for j, score_and_index in enumerate(scores_with_indexes):
            _, i = score_and_index
            if j == 0:
                answer[i] = 'Gold Medal'
            elif j == 1:
                answer[i] = 'Silver Medal'
            elif j == 2:
                answer[i] = 'Bronze Medal'
            else:
                answer[i] = str(j+1)
        return answer
