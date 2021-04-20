'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
'''
#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        '''
        compare the depth between left sub tree and right sub tree.
        A, If it is equal, it means the left sub tree is a full binary tree
        B, It it is not , it means the right sub tree is a full binary tree
        O(lgn * lgn) time
        '''

        if not root:
            return 0

        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        # print(leftDepth, rightDepth)
        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        # print("in getdepth", root.val, 1 + self.getDepth(root.left))
        return 1 + self.getDepth(root.left)


# @lc code=end
