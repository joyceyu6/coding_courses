
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
'''
#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        if root == None:
            return []

        q = deque([root])
        result = []

        while q:
            temp = []
            l = len(q)
            count = 1
            while count <= l:
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                temp.append(current.val)
                count += 1
            result.append(temp)

        return result

        # @lc code=end
