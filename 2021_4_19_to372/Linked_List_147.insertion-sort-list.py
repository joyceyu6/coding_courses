#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        new_list_head = head
        new_list_tail = new_list_head
        current = new_list_head.next
        new_list_head.next = None
        new_list_tail.next = None

        while current:
            current_next = current.next
            current.next = None
            if current.val <= new_list_head.val:  # if less than head
                current.next = new_list_head
                new_list_head = current
            elif current.val >= new_list_tail.val:  # if greater than tail
                new_list_tail.next = current
                new_list_tail = current
            else:
                # insert in between, no change to head/tail
                search_list = new_list_head
                prev = new_list_head
                while current.val > search_list.val:
                    prev = search_list
                    search_list = search_list.next
                prev.next = current
                current.next = search_list
            current = current_next

        return new_list_head

        # @lc code=end
