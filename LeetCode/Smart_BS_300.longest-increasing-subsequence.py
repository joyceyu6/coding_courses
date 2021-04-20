'''
Given an integer array nums, return the length of the longest strictly 
increasing subsequence.

A subsequence is a sequence that can be derived from an array by 
deleting some or no elements without changing the order of the remaining 
elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
'''
'''
the idea extends to:

initial sub = [ ].
traversing the nums:
a) if val > sub's all elements, then subsequence length increased by 1, 
sub.append(val);
b) if sub[i-1] < val < sub[i], then we find a smaller value, 
update sub[i] = val. Some of the elements stored in the sub[ ] are known 
subsequences, and the other part is elements of other possible new subsequences. 
However, the length of the known subsequences is unchanged.
return the sub[ ]'s length.
'''
'''
Here is the solution's track, as we have nums = [8, 2, 5, 1, 6, 7, 9, 3],
when we traversing the nums:

i = 0,    sub = [8]
i = 1,    sub = [2]
i = 2,    sub = [2, 5]
i = 3,    sub = [1, 5],    
# element has been changed, but the sub's length has not changed.
i = 4,    sub = [1, 5, 6]
i = 5,    sub = [1, 5, 6, 7]
i = 6,    sub = [1, 5, 6, 7, 9]
i = 7,    sub = [1, 3, 6, 7, 9]    
#done! Although the elements are not correct, but the length is correct.
'''


#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for val in nums:
            pos = self.binarySearch(sub, val)
            if pos == len(sub):
                sub.append(val)
            else:
                sub[pos] = val
        return len(sub)

    def binarySearch(self, sub, val):  # O(nlogn) time
        lo, hi = 0, len(sub)-1
        while(lo <= hi):
            mid = lo + (hi - lo)//2
            if sub[mid] < val:
                lo = mid + 1
            elif val < sub[mid]:
                hi = mid - 1
            else:
                return mid
        return lo

        # @lc code=end
