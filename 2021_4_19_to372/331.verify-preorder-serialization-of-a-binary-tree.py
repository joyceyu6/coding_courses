'''
One way to serialize a binary tree is to use pre-order traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #
For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a correct preorder traversal serialization of a binary tree. Find an algorithm without reconstructing the tree.

Each comma separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid, for example it could never contain two consecutive commas such as "1,,3".
'''

#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#

# @lc code=start


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        preorder = preorder.split(',')
        for i in range(len(preorder)):
            print("stack", stack)
            s = preorder[i]
            stack.append(s)

            while stack[-1] == "#":

                print("before", stack, s)
                if len(stack) >= 2 and stack[-2] == "#":
                    stack.pop()
                    stack.pop()
                    if len(stack) > 0:
                        stack.pop()
                        stack.append("#")
                    print("after", stack)
                else:
                    break

        print(stack)
        if len(stack) == 1 and stack[-1] == "#":
            return True
        return False


# @lc code=end
