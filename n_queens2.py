class Solution:
    def totalNQueens(self, n: int) -> int:
        col_set = set()
        pos_diag_set = set()
        neg_diag_set = set()
        num_solutions = 0

        def solve(row: int) -> None:
            if row == n:
                nonlocal num_solutions
                num_solutions += 1
                return
            for col in range(n):
                if col in col_set or row+col in pos_diag_set or row-col in neg_diag_set:
                    continue
                col_set.add(col)
                pos_diag_set.add(row+col)
                neg_diag_set.add(row-col)
                solve(row+1)
                col_set.remove(col)
                pos_diag_set.remove(row+col)
                neg_diag_set.remove(row-col)

        solve(0)
        return num_solutions


solution = Solution()
n = 4
assert solution.totalNQueens(n) == 2
