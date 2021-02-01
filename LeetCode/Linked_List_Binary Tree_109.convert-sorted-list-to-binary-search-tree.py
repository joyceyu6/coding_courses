'''
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
'''
#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # figure out the length of the linked list

        return self.recursive(head)

    def recursive(self, head):
        if not head:
            return None

        if head.next == None:  # if only one node, no left/right
            return TreeNode(head.val)

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        prev = ListNode(0)  # need dummy
        prev.next = head

        current = head
        count = 0
        while count < length // 2:  # no "="
            count += 1
            prev = current
            current = current.next

        prev.next = None
        root = TreeNode(current.val)
        root.left = self.recursive(head)  # line 29 to excl. when no left
        root.right = self.recursive(current.next)
        prev.next = current  # restore but not needed

        return root


# @lc code=end
