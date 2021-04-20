#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        fast_step = 0

        while fast:
            if fast_step > n:  # the one prior to the one to be cut, note off-by-one error
                slow = slow.next
            fast_step += 1
            fast = fast.next

        if fast_step == n:  # critical: corner case: if head is the one to be removed
            return head.next

        # may raise exception if fast_step < n

        slow.next = slow.next.next

        return head


# @lc code=end
