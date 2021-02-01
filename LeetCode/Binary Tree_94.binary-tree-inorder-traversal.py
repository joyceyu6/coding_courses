'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
'''
#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    #     # option 1 : recursive
    #     result = []
    #     self.recursive(root, result)
    #     return result

    # def recursive(self, root, result):
    #     if not root:
    #         return

    #     self.recursive(root.left, result)
    #     result.append(root.val)
    #     self.recursive(root.right, result)

    # option 2 : iterative
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        if not root:
            return root

        q = deque([root])
        result = []
        covered_list = set()  # add this to avoid dulicately adding nodes

        while len(q) > 0:
            current = q[-1]

            if current.left and current.left not in covered_list:
                q.append(current.left)
                covered_list.add(current.left)
                continue

            result.append(current.val)
            q.pop()

            if current.right and current.right not in covered_list:
                q.append(current.right)
                covered_list.add(current.right)
                continue

        return result

        # @lc code=end
