#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.recursive(s, [], result)
        return result

    def recursive(self, s, temp, result):

        if len(s) == 0:
            if len(temp) == 4:
                # temp[:]? no need as use join_temp not temp
                join_temp = '.'.join(temp)
                result.append(join_temp)

            return

        if len(temp) > 4:
            return

        temp.append(s[0])
        self.recursive(s[1:], temp, result)
        temp.pop()

        if s[0] != "0":
            if len(s) >= 2:  # otherwise out of range
                temp.append(s[0:2])
                self.recursive(s[2:], temp, result)
                temp.pop()

            if len(s) >= 3:  # otherwise out of range
                if int(s[0:3]) <= 255:
                    temp.append(s[0:3])
                    self.recursive(s[3:], temp, result)
                    temp.pop()

            # @lc code=end
