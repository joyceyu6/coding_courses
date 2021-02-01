#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_dummy = ListNode(0)
        right_dummy = ListNode(0)

        left_tail = left_dummy
        right_head = right_dummy
        right_tail = right_dummy

        while head:
            current = head
            if current.val < x:
                left_tail.next = current
                left_tail = left_tail.next

            else:
                right_tail.next = current
                right_tail = right_tail.next

            head = head.next

        left_tail.next = right_head.next  # right_head.next not right_head
        right_tail.next = None  # cut off the rest
        return left_dummy.next

# @lc code=end
