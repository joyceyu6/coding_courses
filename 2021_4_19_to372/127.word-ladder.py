#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
'''
import string
from collections import deque


class GraphNode:
    def __init__(self, nodeVal):
        self.nodeVal = nodeVal
        self.neighbors = []

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def getNeighbors(self):
        return self.neighbors

    def getNodeValue(self):
        return self.nodeVal


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # construct graph:

        dic = {}  # critical, dic to store nodes

        if beginWord not in wordList:
            wordList.append(beginWord)

        for word in wordList:
            node = GraphNode(word)
            dic[word] = node

        for word in wordList:
            for i in range(len(word)):
                # change one at a time for 26 letters
                for c in list(string.ascii_lowercase):
                    candidate = word[:i] + c + word[i+1:]
                    if candidate != word and candidate in dic:  # note 1st condition
                        dic[word].addNeighbor(dic[candidate])

        # breadth first search

        ladder_count = 0

        visited = set()
        to_visit = deque([dic[beginWord]])
        while to_visit:
            current_len = len(to_visit)
            ladder_count += 1
            for _ in range(current_len):
                current_node = to_visit.popleft()
                if current_node.getNodeValue() == endWord:
                    return ladder_count
                if current_node in visited:
                    continue
                visited.add(current_node)

                to_visit.extend(current_node.getNeighbors())

        return 0

    # @lc code=end
