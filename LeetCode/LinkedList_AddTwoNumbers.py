'''
2. Add Two Numbers (Medium)
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

# ListNode, dummy head for new list, logic

# Definition for singly-linked list.\


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        while l1 != None or l2 != None or carry != 0:  # critical
            sum_val = 0
            if l1 != None:
                sum_val += l1.val
                l1 = l1.next

            if l2 != None:
                sum_val += l2.val
                l2 = l2.next

            sum_val += carry
            carry = sum_val // 10

            new_node = ListNode(sum_val % 10)
            current.next = new_node
            current = current.next

        return dummy_head.next


solution = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))
result = solution.addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next
