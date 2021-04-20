'''
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [x for x in range(numCourses)]

        # construct graph
        # find starting point/only when no prerequisit
        dic = {}
        num_prerequisite = {}  # in_degree/prerequisits count
        for i in range(numCourses):
            num_prerequisite[i] = 0  # initial dictionary definition

        # count each course's prerequisites
        for courses in prerequisites:
            self.add_graph(dic, courses[0], courses[1])
            num_prerequisite[courses[0]] += 1

        # find loop/cycle w BFS
        q = deque([])
        visited = set()
        result = []

        # add nodes without prerequisits/add to queue only when no prerequisites
        for course in num_prerequisite:
            if num_prerequisite[course] == 0:
                q.append(course)

        # if len(q) = 0:
        #     return False

        while len(q) > 0:
            l = len(q)
            for i in range(l):
                current = q.popleft()
                result.append(current)
                visited.add(current)
                if current not in dic:
                    continue  # no prerequisites

                for next_course in dic[current]:
                    num_prerequisite[next_course] -= 1
                    if num_prerequisite[next_course] == 0:
                        # add to queue only when no prerequisites
                        q.append(next_course)

        if len(visited) == numCourses:
            return result
        return []

    # construct directional graph

    def add_graph(self, dic, course, pre_course):
        if pre_course not in dic:
            dic[pre_course] = []

        dic[pre_course].append(course)


# @lc code=end
