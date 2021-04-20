#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        dic = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

        listToadd = [0 for i in range(len(num1) + len(num2))]

        for i in range(len(num1)):
            for j in range(len(num2)):
                position = i + j
                num1_digit = dic[num1[len(num1)-1-i]]
                num2_digit = dic[num2[len(num2)-1-j]]
                listToadd[position] += num1_digit * num2_digit

        carryover = 0
        new_carryover = 0
        for i in range(len(listToadd)):
            new_carryover = (listToadd[i] + carryover) // 10
            listToadd[i] = (listToadd[i] + carryover) % 10
            carryover = new_carryover

        result = ""
        for i in range(len(listToadd)):
            if i == len(listToadd) - 1 and listToadd[i] == 0:
                continue
            result += str(listToadd[i])

        return result[::-1]

        '''
            "123" * "456"
            use this logic:
            
            [18,27,28,13,4,0]
            ...
            [8,8,0,6,5,0]
            "88065"
            "56088"


            too awkward:
            "123" * "456"
            [0,0,0,0,0,0]
            [0,0,0,6,12,18]
            [0,0,5,10+6,15+12,18]
            [0,4,5+8,12+10+6,15+12,18]

            [0,4,13,28,27,18]
            [0,4,13,28,28,8]
            [0,4,13,30,8,8]
            [0,4,16,0,8,8]
            [0,5,6,0,8,8]

        '''

        # @lc code=end


solution = Solution()
print(solution.multiply("123", "456"))
