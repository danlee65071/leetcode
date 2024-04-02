from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        sorted_candidates = sorted(candidates)

        def findCombinations(pos: int, cur_combination: List[int], cur_sum: int):
            if cur_sum == target:
                combinations.append(cur_combination.copy())
                return
            if pos >= len(candidates) or cur_sum > target:
                return
            prev = -1
            for i in range(pos, len(candidates)):
                if sorted_candidates[i] == prev:
                    continue
                cur_combination.append(sorted_candidates[i])
                findCombinations(i+1, cur_combination, cur_sum+sorted_candidates[i])
                cur_combination.pop()
                prev = sorted_candidates[i]

        findCombinations(0, [], 0)
        return combinations


solution = Solution()
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(solution.combinationSum2(candidates, target))
candidates = [2, 5, 2, 1, 2]
target = 5
print(solution.combinationSum2(candidates, target))
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30
print(solution.combinationSum2(candidates, target))
