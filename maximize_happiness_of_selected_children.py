from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sorted_happiness = sorted(happiness, reverse=True)
        max_k_happiness = 0
        for i in range(k):
            cur_happiness = max(sorted_happiness[i] - i, 0)
            max_k_happiness += cur_happiness
        return max_k_happiness
