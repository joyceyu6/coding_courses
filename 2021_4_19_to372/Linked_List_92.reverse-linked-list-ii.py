#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy_head = ListNode(0)
        dummy_head.next = head
        slow = dummy_head
        fast = head
        count = 1

        while count < n:
            if count < m:
                slow = slow.next
            fast = fast.next
            count += 1

        # exit when fast at n, slow at m - 1

        left_head = slow
        prev = slow
        current = slow.next

        count = m
        # reverse m to n
        while count <= n:

            current_next = current.next

            current.next = prev

            prev = current
            current = current_next
            count += 1

        left_head.next.next = current  # tricky
        left_head.next = prev

        return dummy_head.next

        # @lc code=end
