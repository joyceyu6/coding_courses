'''
Given a singly linked list, group all odd nodes together 
followed by the even nodes. Please note here we are talking 
about the node number and not the value in the nodes.

You should try to do it in place. The program should run in 
O(1) space complexity and O(nodes) time complexity.
'''
'''
Constraints:

The relative order inside both the even and odd groups should remain 
as it was in the input.
The first node is considered odd, the second node even and so on ...
The length of the linked list is between [0, 10^4].
'''

#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        odd_head = ListNode(0)
        even_head = ListNode(0)
        odd_tail = odd_head
        even_tail = even_head

        # even_head, even_tail, odd_head, odd_tail = head, head, head, head
        is_odd = False
        while head:

            if is_odd:  # odd
                odd_tail.next = head
                odd_tail = odd_tail.next

            else:  # even

                even_tail.next = head
                even_tail = even_tail.next

            head = head.next
            is_odd = not is_odd

        even_tail.next = odd_head.next
        odd_tail.next = None

        return even_head.next

        # @lc code=end
