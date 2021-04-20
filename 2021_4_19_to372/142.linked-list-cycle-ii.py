
#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow_count = 0
        fast_count = 0
        slow = head
        fast = head

        while True:
            print(fast.val, slow.val)
            if slow == fast and slow_count != fast_count:
                break
            if fast == None or fast.next == None:  # no circle
                return None
            fast = fast.next.next
            fast_count += 2
            slow = slow.next
            slow_count += 1

        gap = fast_count - slow_count

        slow_count = 0
        fast_count = 0
        slow = head
        fast = head

        while True:
            if slow == fast and slow_count != fast_count:
                break
            if fast_count > gap:
                slow = slow.next
                slow_count += 1
            fast = fast.next
            fast_count += 1

        return slow


# @lc code=end
