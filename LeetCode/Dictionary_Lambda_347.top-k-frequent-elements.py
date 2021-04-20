'''
Given an integer array nums and an integer k, return the k most frequent 
elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.legth <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
'''
#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= 1:
            return nums

        dic = {}
        for n in nums:
            if n in dic:
                dic[n] += 1
                continue
            dic[n] = 1

        new_dic = dict(
            sorted(dic.items(), key=lambda item: item[1], reverse=True))
        # {k:v for k,v in sorted(dic.items(),key=lambda item: item[1])}
        # items.sort(key=lambda item: item[1])  # lambda

        result = []
        for key in new_dic:
            if len(result) == k:
                break
            result.append(key)
        return result

# @lc code=end


'''
[-1,-1]\n1
[3,0,1,0]\n1
'''
