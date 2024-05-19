from typing import List
from functools import lru_cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # # top-down
        # if len(jobDifficulty) < d:
        #     return -1
        # hardest_job_remaining: List[int] = [0] * len(jobDifficulty)
        # hardest_job: int = 0
        # for i in range(len(jobDifficulty)-1, -1, -1):
        #     hardest_job = max(hardest_job, jobDifficulty[i])
        #     hardest_job_remaining[i] = hardest_job

        # @lru_cache(None)
        # def dp(i: int, day: int) -> int:
        #     if d == day:
        #         return hardest_job_remaining[i]
        #     hardest: int = 0
        #     best: float = float('inf')
        #     for j in range(i, len(jobDifficulty) - (d - day)):
        #         hardest = max(jobDifficulty[i: j+1])
        #         best = min(best, hardest + dp(j+1, day+1))
        #     return best

        # return dp(0, 1)
        #  bottom-up
        if len(jobDifficulty) < d:
            return -1
        dp: List[float] = [[float('inf')] * (d + 1) for i in range(len(jobDifficulty))]
        dp[-1][d] = jobDifficulty[-1]
        for i in range(len(jobDifficulty) - 2, -1, -1):
            dp[i][d] = max(jobDifficulty[i], dp[i+1][d])
        for day in range(d - 1, 0, -1):
            for i in range(day - 1, len(jobDifficulty) - (d - day)):
                hardest: int = 0
                for j in range(i, len(jobDifficulty) - (d - day)):
                    hardest = max(hardest, jobDifficulty[j])
                    dp[i][day] = min(dp[i][day], hardest + dp[j+1][day+1])
        return dp[0][1]


solution: Solution = Solution()
jobDifficulty: List[int] = [6, 5, 4, 3, 2, 1]
d: int = 2
assert solution.minDifficulty(jobDifficulty, d) == 7
