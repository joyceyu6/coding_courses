'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''
#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []  # corner case

        result = []
        q = deque([root])

        while q:
            l = len(q)
            for i in range(l):
                current = q.popleft()
                if i == l - 1:
                    result.append(current.val)
                if current.left != None:
                    q.append(current.left)
                if current.right != None:
                    q. append(current.right)
        return result

        # @lc code=end
