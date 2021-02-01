'''
1. Two Sum (Easy                                                                         )
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

from typing import List  # type hint


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # O(n) complexity, memory = O(n)
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i

        for g in range(len(nums)):  # better use i,j,k as index
            find_number = target - nums[g]  # candidate would be a better name
            if find_number in dic:
                if dic[find_number] != g:  # critical: same number cannot use twice
                    return([g, dic[find_number]])


solution = Solution()  # declare an instance
print(solution.twoSum([3, 3], 6))

# extended questions:
# what if not found - return special value or raise Exception('xxx')
