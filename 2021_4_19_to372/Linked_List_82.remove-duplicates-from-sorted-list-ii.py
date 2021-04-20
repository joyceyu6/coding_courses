#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        result = dummy  # need create new dummy otherwise dummy always the last node

        if not head:
            return head

        prior = head
        count = 0

        while head:
            current = head

            if current.val != prior.val:
                if count == 1:
                    result.next = ListNode(prior.val)  # create new node
                    result = result.next  # move result ahead
                count = 1
                prior = current
                head = head.next
                continue

            count += 1
            prior = current
            head = head.next

        if count == 1:
            result.next = ListNode(prior.val)  # will miss one when exit

        return dummy.next


# @lc code=end
