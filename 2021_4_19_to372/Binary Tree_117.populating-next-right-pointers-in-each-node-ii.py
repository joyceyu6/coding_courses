'''
Given a binary tree

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
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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
# option 1: lg(n) memory; cannot use recursive as compared to perfect balanced tree: need finish one level then go to next
# move previous level node - iterate, current level node - connect, next level node - store head

# [1,2,3,4,5,null,6,7,null,null,null,null,8]


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        current_node = root
        pre_level_node = None

        while current_node != None:
            next_level_head = None
            # prev level start
            current_level_head = current_node  # current level start

            if pre_level_node == None:  # so this is root/corner case
                pre_level_node = current_node
                current_node = root.left if root.left != None else root.right

                continue

            pre_node = None  # current level to be stored
            while pre_level_node != None:
                if pre_level_node.left != None and pre_level_node.right != None:
                    pre_level_node.left.next = pre_level_node.right

                    if pre_node != None:
                        pre_node.next = pre_level_node.left

                    pre_node = pre_level_node.right  # tail of completed

                    if next_level_head == None:
                        next_level_head = pre_level_node.left
                elif pre_level_node.left != None:
                    if pre_node != None:
                        pre_node.next = pre_level_node.left

                    pre_node = pre_level_node.left
                    if next_level_head == None:
                        next_level_head = pre_level_node.left
                elif pre_level_node.right != None:
                    if pre_node != None:
                        pre_node.next = pre_level_node.right

                    pre_node = pre_level_node.right

                    if next_level_head == None:
                        next_level_head = pre_level_node.right

                pre_level_node = pre_level_node.next

            pre_level_node = current_level_head
            current_node = next_level_head

        return root

    # def recursive(self, current_node, parent):
    #     if current_node == None:
    #         return

    #     if current_node.right != None and current_node.right != None:
    #         current_node.left.next = current_node.right

    #     if current_node.next == None and parent != None:
    #         direct_parent = parent.next  # start w parent.next then always use direct parent
    #         while direct_parent != None:  # in case current_node.next is many nodes away from parent.next
    #             if current_node.val == 7:
    #                 print(direct_parent.val)
    #             if direct_parent.left == None and direct_parent.right == None:
    #                 direct_parent = direct_parent.next
    #                 continue

    #             if direct_parent.left != None:
    #                 current_node.next = direct_parent.left
    #             else:
    #                 current_node.next = direct_parent.right
    #             break

    #     self.recursive(current_node.left, current_node)
    #     self.recursive(current_node.right, current_node)

        # # option 2 - queque, n/2 memory with n = number of nodes
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
