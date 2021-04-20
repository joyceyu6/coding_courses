'''
Given an integer array nums, reorder it such that 
nums[0] < nums[1] > nums[2] < nums[3]....

You may assume the input array always has a valid answer.
'''

'''
Follow Up: Can you do it in O(n) time and/or in-place with O(1) extra space?
'''


#
# @lc app=leetcode id=324 lang=python3
#
# [324] Wiggle Sort II
#

# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # mid_index = len(nums) // 2  # find median
        # mid = nums[mid_index]
        # # in place sort/3-partitions: <median, median, =median, > median
        # i, j, k = 0, 0, len(nums) - 1
        # while j <= k:
        #     if nums[j] > mid:
        #         nums[i+1], nums[j+1] = nums[j+1], nums[i+1]
        #     elif nums[j] < mid:
        #         nums[j], nums[k-1] = nums[k-1], nums[j]
        #     else:
        #         j += 1

        nums.sort()
        half = len(nums[::2]) - 1
        # smaller on even, larger on odd indexes:
        print(nums, nums[::2], nums[1::2], nums[half::-1], nums[:half:-1])
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]


        # @lc code=end
'''
Option 1: O(n) time and O(1) space:
First I find a median using nth_element. 
That only guarantees O(n) average time complexity and I don't know about space complexity. 
I might write this myself using O(n) time and O(1) space, but that's not what I want to show here.

This post is about what comes after that. We can use three-way partitioning to 
arrange the numbers so that those larger than the median come first, then those equal 
to the median come next, and then those smaller than the median come last.

Ordinarily, you'd then use one more phase to bring the numbers to their final positions 
to reach the overall wiggle-property. But I don't know a nice O(1) space way for this. 
Instead, I embed this right into the partitioning algorithm. That algorithm simply works 
with indexes 0 to n-1 as usual, but sneaky as I am, I rewire those indexes where 
I want the numbers to actually end up. The partitioning-algorithm doesn't even know that 
I'm doing that, it just works like normal (it just uses A(x) instead of nums[x]).

Let's say nums is [10,11,...,19]. Then after nth_element and ordinary partitioning, 
we might have this (15 is my median):

index:     0  1  2  3   4   5  6  7  8  9
number:   18 17 19 16  15  11 14 10 13 12
I rewire it so that the first spot has index 5, the second spot has index 0, etc, 
so that I might get this instead:

index:     5  0  6  1  7  2  8  3  9  4
number:   11 18 14 17 10 19 13 16 12 15
And 11 18 14 17 10 19 13 16 12 15 is perfectly wiggly. 
And the whole partitioning-to-wiggly-arrangement (everything after finding the median) 
only takes O(n) time and O(1) space.
'''

'''option2
put the smaller half of the numbers on the even indexes and the larger half on the odd indexes, both from right to left:
I want:

Odd-index numbers are larger than their neighbors.
Since I put the larger numbers on the odd indexes, clearly I already have:

Odd-index numbers are larger than or equal to their neighbors.
'''
