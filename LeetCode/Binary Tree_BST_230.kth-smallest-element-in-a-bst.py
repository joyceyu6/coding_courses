'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''
'''
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

 

Constraints:

The number of elements of the BST is between 1 to 10^4.
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
'''

#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        result = []
        self.recursive(root, k, [], result)
        return result[0][k-1]

    def recursive(self, root, k, temp, result):
        if not root:
            if len(temp) == k:
                result.append(temp[:])
            return

        if len(temp) == k:
            result.append(temp[:])
            return

        self.recursive(root.left, k, temp, result)
        temp.append(root.val)
        self.recursive(root.right, k, temp, result)


# @lc code=end
