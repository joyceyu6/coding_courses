#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        matrix_string = ["" for _ in range(numRows)]  # only rows matter
        block_size = numRows * 2 - 2
        for i in range(len(s)):
            row = 0
            index = i % block_size
            if index < numRows:
                row = index
            else:
                row = 2*numRows - index - 2  # (r-1) - [index - (r-1)]
            matrix_string[row] += s[i]

        return "".join(matrix_string)

        # @lc code=end
