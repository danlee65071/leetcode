from typing import List


class Solution:
    def printBoard(self, board: List[List[str]]):
        print('Start')
        for row in board:
            print(row)
        print('End')

    def checkBoard(self, board: List[List[str]]):
        for row in board:
            for num in row:
                if num == '.':
                    return False
        return True

    def findFirstSpace(self,  board: List[List[str]]):
        for row_it, row in enumerate(board):
            for col_it, num in enumerate(row):
                if num == '.':
                    return row_it, col_it
        return -1, -1

    def getPossiblesNums(self, board: List[List[str]], x: int, y: int) -> List[int]:
        nums = {str(i) for i in range(1, 10)}
        row_set, col_set, subboard_set = set(), set(), set()
        for num in board[x]:
            if num != '.':
                row_set.add(num)
        for row in board:
            if row[y] != '.':
                col_set.add(row[y])
        for i in range(3 * (x // 3), 3 * (x // 3 + 1)):
            for j in range(3 * (y // 3), 3 * (y // 3 + 1)):
                if board[i][j] != '.':
                    subboard_set.add(board[i][j])
        return sorted(list(nums - row_set.union(col_set, subboard_set)))

    def solve(self, board: List[List[str]], x: int, y: int, nums: List[int]) -> None:
        if self.checkBoard(board):
            self.is_solved = True
            return
        for num in nums:
            if not self.is_solved:
                board[x][y] = num
            new_x, new_y = self.findFirstSpace(board)
            new_nums = self.getPossiblesNums(board, new_x, new_y)
            self.solve(board, new_x, new_y, new_nums)
            if not self.is_solved:
                board[x][y] = '.'

    def solveSudoku(self, board: List[List[str]]) -> None:
        self.is_solved = False
        x, y = self.findFirstSpace(board)
        nums = self.getPossiblesNums(board, x, y)
        self.solve(board, x, y, nums)


solution = Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
solution.solveSudoku(board)
print(board)
