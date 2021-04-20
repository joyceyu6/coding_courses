'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        '''
        solution 2 Pass value from bottom-up
        '''
        is_valid_BST, min_val, max_val = self.recursive(root)
        return is_valid_BST

    def recursive(self, root):
        min_val = root.val
        max_val = root.val

        if root.left:
            left_is_valid, left_min, left_max = self.recursive(root.left)
            if left_is_valid == False:
                return False, 0, 0
            if root.val <= left_max:
                return False, 0, 0
            min_val = left_min

        if root.right:
            right_is_valid, right_min, right_max = self.recursive(root.right)
            if right_is_valid == False:
                return False, 0, 0
            if root.val >= right_min:
                return False, 0, 0
            max_val = right_max

        return True, min_val, max_val

        '''
        solution 1 Pass value from top-down

        '''

    #     # None None as starting point, needs validate in recursifve for existence
    #     if self.recursive(root, None, None) == False:
    #         return False
    #     return True

    # def recursive(self, root, min_val, max_val):
    #     if not root:
    #         return True

    #     if min_val != None and root.val <= min_val:  # min_val could be none
    #         return False

    #     if max_val != None and root.val >= max_val:  # max_val could be none
    #         return False

    #     if self.recursive(root.left, min_val, root.val) == False:  # change max if left-ward
    #         return False

    #     if self.recursive(root.right, root.val, max_val) == False:  # change min if right-ward
    #         return False

    #     return True

        # @lc code=end
