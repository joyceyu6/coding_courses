'''
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
'''


#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return root

        q = deque([root])
        left_to_right = True
        result = []

        while q:
            temp = []
            l = len(q)

            for _ in range(l):
                current = q.popleft()
                temp.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

            if left_to_right:
                result.append(temp)
            else:
                result.append(temp[::-1])

            left_to_right = not left_to_right

        return result

        # @lc code=end
