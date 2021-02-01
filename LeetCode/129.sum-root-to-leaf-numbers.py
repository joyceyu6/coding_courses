#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        nbr_list = []
        self.recursive(root, nbr_list, [])
        result = 0
        for nbr in nbr_list:
            result += nbr
        return result

    def recursive(self, root, nbr_list, temp):
        if root == None:
            if len(temp[:]) != 0:

                int_to_add = 0
                print(temp)
                for i in range(len(temp[:])):
                    if temp[i] == 0:  # 0 need special treatment
                        continue
                    int_to_add = int_to_add * 10 + temp[i]

                if int_to_add not in nbr_list:  # may have duplicates
                    nbr_list.append(int_to_add)
            return

        temp.append(root.val)

        self.recursive(root.left, nbr_list, temp)
        self.recursive(root.right, nbr_list, temp)
        temp.pop()


# @lc code=end
