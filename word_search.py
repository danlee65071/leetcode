from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        paths = set()

        def solve(row: int, col: int, it: int) -> bool:
            if it == len(word):
                return True
            if row < 0 or row >= rows or \
                col < 0 or col >= cols or \
                    (row, col) in paths or board[row][col] != word[it]:
                return False
            paths.add((row, col))
            res = (solve(row+1, col, it+1) or
                   solve(row-1, col, it+1) or
                   solve(row, col+1, it+1) or
                   solve(row, col-1, it+1))
            paths.remove((row, col))
            return res

        for i in range(rows):
            for j in range(cols):
                if solve(i, j, 0):
                    return True
        return False


solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
assert solution.exist(board, word) == True
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
assert solution.exist(board, word) == True
board = [["a"]]
word = "a"
assert solution.exist(board, word) == True
board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word = "aaaaaaaaaaaaa"
assert solution.exist(board, word) == False
