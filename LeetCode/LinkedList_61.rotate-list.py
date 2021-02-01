#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head

        dummy = ListNode(0)
        new_head = head
        fast = head
        slow = head
        step = 1  # start from 1, note off-by-one error
        move_flag = False

        while fast.next:

            if step > k:
                slow = slow.next
                move_flag = True

            fast = fast.next
            step += 1

        # out of loop not to k yet:
        if move_flag == False:
            new_step = k % (step)

            if new_step == 0:
                return head

            current_step = 1
            while current_step < step - new_step:
                slow = slow.next
                current_step += 1

        # out of loop with slow at the node to be rotated from its next node
        dummy.next = slow.next
        fast.next = new_head
        slow.next = None

        return dummy.next


# @lc code=end
