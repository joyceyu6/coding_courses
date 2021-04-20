'''
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum 
of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine 
if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 
1, 2, 03 or 1, 02, 3 is invalid.
'''
#
# @lc app=leetcode id=306 lang=python3
#
# [306] Additive Number
#

# @lc code=start


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        for i in range(1, n):  # i: one digit after first number
            for j in range(i+1, n):  # j: one digit after second number/1st of 3rd nbr

                a = num[:i]  # 1st number
                b = num[i:j]  # 2nd number
                if num[0] == "0" and i != 1:  # no leading zero for 1st number unless 0 itself
                    continue  # "000"--->true
                if num[i] == "0" and j != i + 1:  # no leading zero for 2nd number
                    continue

                prior = a
                current = b
                next_start = j

                while next_start < n:
                    next_shouldbe = str(int(prior) + int(current))
                    next_end = next_start + len(next_shouldbe)  # next end + 1

                    if num[j] == "0" and len(next_shouldbe) != 1:
                        break

                    next = num[next_start:next_end]

                    if next != next_shouldbe:
                        break
                    prior = current
                    current = next
                    next_start = next_end
                    if next_start >= n:
                        return True

        return False


# @lc code=end

solution = Solution()
print(solution.isAdditiveNumber("000"))

'''
"199100199" -->true
'''
'''
"101"-->True
'''
