#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        hit = 1
        hit_count = 1
        result = [0]

        while hit_count <= n:  # hit = 1, 10, 100...
            # use 'hit' to hit every nbr in result in reverse order
            prior_len = len(result)
            for i in range(prior_len-1, -1, -1):
                current = result[i] ^ hit
                result.append(current)

            hit = hit << 1
            hit_count += 1

        return result
        # @lc code=end
