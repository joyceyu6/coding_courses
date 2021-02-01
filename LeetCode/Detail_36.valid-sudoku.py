#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = 9
        col = 9
        sub_r = 3
        sub_c = 3

        for r in range(row):
            set_to_check = set()
            for c in range(col):
                if board[r][c] == ".":
                    continue
                if board[r][c] in set_to_check:
                    return False
                set_to_check.add(board[r][c])

        for c in range(col):
            set_to_check = set()
            for r in range(row):
                if board[r][c] == ".":
                    continue
                if board[r][c] in set_to_check:
                    return False
                set_to_check.add(board[r][c])

        for sub_box_rstart in range(sub_r):
            for sub_box_cstart in range(sub_c):
                r_start = sub_box_rstart * sub_r
                c_start = sub_box_cstart * sub_c
                set_to_check = set()
                for r in range(r_start, r_start + sub_r):
                    for c in range(c_start, c_start + sub_c):
                        if board[r][c] == ".":
                            continue
                        if board[r][c] in set_to_check:
                            return False
                        set_to_check.add(board[r][c])
        return True
        # @lc code=end
