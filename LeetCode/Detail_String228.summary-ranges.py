'''
ou are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
'''
#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        i = 0
        result = []
        start = 0

        while i < len(nums) - 1:
            if nums[i] + 1 != nums[i+1]:
                result.append(self.printRange(nums[start], nums[i]))
                start = i+1
            i += 1

        # add the last one
        result.append(self.printRange(nums[start], nums[i]))
        return result

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)

# @lc code=end
