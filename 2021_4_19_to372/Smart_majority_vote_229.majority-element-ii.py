

'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Follow-up: Could you solve the problem in linear time and in O(1) space?
'''
'''
	Majority voting algorithm/Boyer–Moore string-search algorithm:
	https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
'''

#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#

# @lc code=start


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # linear time and O(1) space:
        if len(nums) == 0:
            return []

        count1 = 0
        count2 = 0
        candidate1 = 0
        candidate2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:  # critical
                count1 -= 1
                count2 -= 1

        result = []
        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)
        # [0,0] -->[0]
        if nums.count(candidate2) > len(nums) // 3 and candidate2 != candidate1:
            result.append(candidate2)
        return result

        # @lc code=end
