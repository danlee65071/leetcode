from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def findCominations(position: int, current_combination: List, current_sum: int):
            if current_sum == target:
                combinations.append(current_combination.copy())
                return
            if position >= len(candidates) or current_sum > target:
                return
            current_combination.append(candidates[position])
            findCominations(position, current_combination, current_sum + candidates[position])
            current_combination.pop()
            findCominations(position + 1, current_combination, current_sum)
        
        findCominations(0, [], 0)

        return combinations


solution = Solution()
candidates = [2,3,6,7]
target = 7
print(solution.combinationSum(candidates, target))
