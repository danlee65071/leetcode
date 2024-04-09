from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        board = [['.' for __ in range(n)] for _ in range(n)]
        col_set = set()
        pos_diag = set()
        neg_diag = set()

        def solve(row: int) -> None:
            if row == n:
                solutions.append([''.join(row) for row in board])
                return
            for col in range(n):
                if col in col_set or row + col in pos_diag or row - col in neg_diag:
                    continue
                col_set.add(col)
                pos_diag.add(row+col)
                neg_diag.add(row-col)
                board[row][col] = 'Q'
                solve(row+1)
                col_set.remove(col)
                pos_diag.remove(row+col)
                neg_diag.remove(row-col)
                board[row][col] = '.'

        solve(0)
        return solutions


solution = Solution()
n = 4
assert solution.solveNQueens(n) == [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
