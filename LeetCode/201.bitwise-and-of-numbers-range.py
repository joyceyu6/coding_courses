#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0

        list_ones = [-1 for _ in range(31)]  # default must not be 1
        for i in range(m, n+1):
            current = i
            count = 0
            while count <= 30:  # cannot use current!=0 will miss
                if list_ones[count] == 0:
                    current = current >> 1
                    count += 1
                    continue
                if current & 1 == 0:
                    list_ones[count] = 0
                else:
                    list_ones[count] = 1
                current = current >> 1
                count += 1

        result = 0
        for j in range(len(list_ones)-1, -1, -1):
            if list_ones[j] == -1:  # all -1 is 0
                list_ones[j] = 0
            result += list_ones[j]
            if j != 0:
                result = result << 1
        return result


# @lc code=end
'''
time limit exceeded
20000
2147483647
expected 0

'''
