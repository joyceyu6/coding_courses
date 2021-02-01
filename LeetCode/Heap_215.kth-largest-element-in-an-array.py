'''
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
'''

#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapq is a binary heap, with O(log n) push and O(log n) pop
        # heapq.heapify(nums)
        h = []
        # O(n log n) to push all the items onto the heap
        for num in nums:
            # reverse sign so the min heap can pop largest nbr
            heappush(h, -num)  # duplicate allowed
        for i in range(len(h)):
            # or min heap then pop out len(nums) - k which is O((n-k) log n) complexity, O(n) extra space
            current = heappop(h)
            if i == k-1:  # note off by one error
                return -current

        # @lc code=end
