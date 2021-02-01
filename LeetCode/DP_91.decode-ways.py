#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    '''
    solution 1: recursive without simplification/dp:
    '''
    # def numDecodings(self, s: str) -> int:

    #     return self.recursive(s)

    # def recursive(self, s: str) -> int:
    #     if len(s) == 0:
    #         return 1

    #     if s[0] == "0":
    #         return 0

    #     count = 0

    #     count += self.recursive(s[1:])

    #     if len(s) >= 2 and int(s[:2]) <= 26:
    #         count += self.recursive(s[2:])

    #     return count

    '''
    solution 2: memorization with dictionary
    string and number are value variables that won't change when reference variables change
    '''

    # def numDecodings(self, s: str) -> int:
    #     dic = {}

    #     count = self.recursive(s, dic)
    #     return count

    # def recursive(self, s: str, dic) -> int:
    #     if len(s) == 0:
    #         return 1

    #     if s in dic:
    #         return dic[s]

    #     if s[0] == "0":
    #         dic[s] = 0
    #         return 0

    #     count = 0  # value variable

    #     count += self.recursive(s[1:], dic)

    #     if len(s) >= 2 and int(s[:2]) <= 26:
    #         count += self.recursive(s[2:], dic)

    #     dic[s] = count
    #     return count

    '''
    solution 3: dynamic programming
    '''

    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]  # len + 1
        dp[-1] = 1

        for i in range(len(s)-1, -1, -1):
            if i == len(s) - 1:
                if s[i] == "0":
                    dp[i] = 0
                else:
                    dp[i] = 1
                continue

            # if i == len(s) - 2:
            #     if s[i] == "0":
            #         dp[i] = 0
            #     else:
            #         if int(s[i:]) <= 26:
            #             dp[i] += 1
            #         dp[i] += dp[i+1]
            #     continue

            if s[i] == "0":
                dp[i] = 0
            else:

                if int(s[i:i+2]) <= 26:
                    dp[i] += dp[i+2]
                dp[i] += dp[i+1]
        return dp[0]

        # @lc code=end
solution = Solution()
solution.numDecodings("226")
