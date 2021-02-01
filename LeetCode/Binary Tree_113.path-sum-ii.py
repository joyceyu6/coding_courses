'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
'''
#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        result = []
        self.recursive(root, [root.val], result, sum -
                       root.val)  # incl. root here
        return result

    def recursive(self, root, temp, result, sum):

        if (not root.left) and (not root.right):  # no child, i.e., no left no right child
            if sum == 0:
                result.append(temp[:])
            return

        # if sum < 0:
        #     return

        if root.left:
            temp.append(root.left.val)
            self.recursive(root.left, temp, result, sum - root.left.val)
            temp.pop()

        if root.right:
            temp.append(root.right.val)
            self.recursive(root.right, temp, result, sum - root.right.val)
            temp.pop()


'''
[1,2]
1
return [[1]], expected []
'''


# @lc code=end
