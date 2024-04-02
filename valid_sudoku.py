from typing import List


class Solution:
    # def isValidSudoku(self, board: List[List[str]]) -> bool:
    #     cols_map = {i: set() for i in range(9)}
    #     subboards_map = {i: set() for i in range(3)}
    #     for row_it, row in enumerate(board):
    #         if row_it != 0 and row_it % 3 == 0:
    #             subboards_map = {i: set() for i in range(3)}
    #         row_set = set()
    #         for col, num in enumerate(row):
    #             subboard_it = col // 3
    #             if num != '.' and (num in cols_map[col] or num in row_set or
    #                                num in subboards_map[subboard_it]):
    #                 return False
    #             cols_map[col].add(num)
    #             row_set.add(num)
    #             subboards_map[subboard_it].add(num)
    #     return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_set = set()
        for row_it, row in enumerate(board):
            for col_it, num in enumerate(row):
                if num != '.' and (row_it, num) not in board_set and \
                        (num, col_it) not in board_set and \
                            (row_it // 3, col_it // 3, num) not in board_set:
                    board_set.add((row_it, num))
                    board_set.add((num, col_it))
                    board_set.add((row_it // 3, col_it // 3, num))
                elif num != '.':
                    return False
        return True


solution = Solution()
board = \
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))
board = \
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(solution.isValidSudoku(board))
