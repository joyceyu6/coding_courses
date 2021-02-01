#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # similar to list quick sort w nlg(n) complexity
        # must optimize: 1. euqal_node 2. find the right pivot/mid
        if head == None or head.next == None:
            return head

        dummy_smaller = ListNode(0)
        dummy_bigger = ListNode(0)

        smaller_node = dummy_smaller
        bigger_node = dummy_bigger

        # optimize 2: pick pivot from middle of list - critical otherwise time limit exceeded
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        slow_next = slow.next
        pivot_node = head  # true corner case
        if slow_next != None:  # critical not to exceed time limit
            pivot_node = slow.next
            slow.next = slow_next.next
            pivot_node.next = head  # must exchange pivot and head
            head = pivot_node  # now pivot becomes new head

        # put node smaller/bigger than pivot to smaller_/bigger_node
        equal_node = pivot_node  # optimize 1

        current = head.next
        while current != None:
            current_next = current.next
            current.next = None

            if current.val < pivot_node.val:
                smaller_node.next = current
                smaller_node = current
            elif current.val == pivot_node.val:  # optimize 1
                equal_node.next = current
                equal_node = current
            else:
                bigger_node.next = current
                bigger_node = current

            current = current_next

        # recursive
        sorted_smaller = self.sortList(dummy_smaller.next)
        sorted_bigger = self.sortList(dummy_bigger.next)

        # connect smaller_node, equal_node, bigger_node
        if sorted_smaller == None:  # corner case
            equal_node.next = sorted_bigger  # now pivotal_node is head of equal_node
            # pivot_node.next = sorted_bigger
            return pivot_node

        current = sorted_smaller
        while current.next != None:
            current = current.next
        current.next = pivot_node
        equal_node.next = sorted_bigger
        # pivot_node.next = sorted_bigger

        return sorted_smaller

# @lc code=end
