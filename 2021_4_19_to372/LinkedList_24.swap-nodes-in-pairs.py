#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        # if head == None:  # corner case not needed w line 26
        #     return head

        dummy = ListNode(0)
        dummy.next = head

        current = head
        prior = dummy  # critical

        while current and current.next:  # current cannot be none as we move two steps at a time

            cnn = current.next.next

            prior.next = current.next
            current.next.next = current
            current.next = cnn

            prior = current
            current = current.next

        return dummy.next


# @lc code=end
