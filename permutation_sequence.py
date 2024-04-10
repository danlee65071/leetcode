from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        permutations = []

        def findPermutations(cur_permutation: str, remains: List[str]) -> None:
            if not remains:
                nonlocal k
                if len(permutations) != k:
                    permutations.append(cur_permutation)
                return
            for str_num in remains:
                if len(permutations) == k:
                    return
                new_remains = [val for val in remains if val != str_num]
                findPermutations(cur_permutation + str_num, new_remains)

        findPermutations('', [str(num) for num in range(1, n+1)])
        return permutations[-1]


solution = Solution()
n = 3
k = 3
assert solution.getPermutation(n, k) == '213'
n = 4
k = 9
assert solution.getPermutation(n, k) == '2314'
n = 3
k = 1
assert solution.getPermutation(n, k) == '123'
