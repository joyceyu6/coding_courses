'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 

Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
'''

#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# option 1 - constant space with recursive call/stack/depth-first; memory: lg(n)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root

        self.recursive(root, None)
        return root

    def recursive(self, current_node, parent):
        if current_node == None:
            return

        if current_node.left and current_node.right:
            current_node.left.next = current_node.right

        if current_node.next == None and parent != None and parent.next != None:  # excl. starting root
            current_node.next = parent.next.left  # infer current_node.next from prior level

        self.recursive(current_node.left, current_node)
        self.recursive(current_node.right, current_node)

        # option 2 - use queue, not constant space though/breadth-first; memory: O(n) or n/2 w n = total nbr

        # from collections import deque
        # class Solution:
        #     def connect(self, root: 'Node') -> 'Node':
        #         if root == None:
        #             return root  # corner case don't forget

        #         q = deque([root])

        #         while q:

        #             breadth = len(q)
        #             count = 1
        #             prior = Node(None)

        #             while count <= breadth:
        #                 current = q.popleft()
        #                 if current.left:
        #                     q.append(current.left)
        #                 if current.right:
        #                     q.append(current.right)

        #                 prior.next = current
        #                 prior = current

        #                 if count == breadth:
        #                     current.next = None

        #                 count += 1

        #         return root

        # @lc code=end
