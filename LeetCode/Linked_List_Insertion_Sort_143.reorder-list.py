'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
'''
#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None:  # corner case
            return head

        # cut off the right part
        measure_head = head
        link_len = 0
        while measure_head != None:
            link_len += 1
            measure_head = measure_head.next

        if link_len <= 2:  # corner case
            return head

        left_tail = head
        cut_index = 0
        while cut_index < link_len // 2:
            left_tail = left_tail.next
            cut_index += 1
        right_head = left_tail.next
        left_tail.next = None

        # reverse the right part
        dummy = ListNode(0)
        dummy.next = right_head
        prev = dummy
        current = right_head
        while current and current.next:
            next = current.next
            current.next = prev
            prev = current
            current = next
        current.next = prev

        # iterate left and right, one left one right
        left = head
        right = current
        count = 0
        while count < link_len - link_len//2 - 1:  # '<' - note off-by-one error
            left_next = left.next
            right_next = right.next
            left.next = right
            right.next = left_next
            left = left_next
            right = right_next
            count += 1

            # @lc code=end
