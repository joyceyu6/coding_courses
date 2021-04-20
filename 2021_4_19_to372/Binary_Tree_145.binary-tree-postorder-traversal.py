'''
Given the root of a binary tree, return the postorder traversal of its nodes' values.
Follow up:

Recursive solution is trivial, could you do it iteratively?
'''

#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.recursive(root, result)
        return result

    def recursive(self, root, result):
        if root == None:
            return

        self.recursive(root.left, result)
        self.recursive(root.right, result)
        result.append(root.val)


# @lc code=end
