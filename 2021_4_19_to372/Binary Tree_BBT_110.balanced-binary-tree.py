'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        is_balanced, _ = self.recursive(root)
        return is_balanced

    def recursive(self, root):
        if not root:
            return True, 0  # also needs to return depth

        left_result, left_depth = self.recursive(root.left)
        right_result, right_depth = self.recursive(root.right)

        if left_result == False:
            return False, 0
        if right_result == False:
            return False, 0

        if abs(right_depth - left_depth) > 1:
            return False, 0

        # definition of height of the tree
        return True, max(left_depth, right_depth)+1


# @lc code=end
