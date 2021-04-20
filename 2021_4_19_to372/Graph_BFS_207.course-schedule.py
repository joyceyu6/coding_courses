'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''
#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start

# option 2 - DFS: corner case: if one part with cycle the other doesn't
# option1 - BFS: add to queue only when no dependents/prerequisits/all prerequists are taken
# both needs to identify a starting point and make sure no missing nodes

from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # option 2: DFS

        # 3\n[[1,0]]
        # 8\n[[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]]-->False
        # 5\ [[1,0],[2,1],[3,4],[4,3]]

        if len(prerequisites) == 0:
            return True

        roots = set(range(numCourses))  # use this to identify starting point
        courses_exist = set()

        # translate to graph
        dic = {}

        for pair in prerequisites:
            course_number = pair[0]
            pre_course = pair[1]
            courses_exist.add(course_number)
            courses_exist.add(pre_course)
            self.add_precourse(course_number, pre_course, dic)
            if course_number in roots:
                # leaving only those without precourse as starting point
                roots.remove(course_number)

        if len(roots) == 0:
            return False  # if no such root identified, e.g. 2\n[[1,0],[0,1]]

        visited = set()  # add global variable
        for course in roots:
            parents = set()
            result = self.DFS(course, dic, visited, parents)
            if result == False:
                return False
        if len(visited) != numCourses:  # critical,e.g. 5\n[[1,4],[4,1],[2,3]]
            return False

        return True

    def DFS(self, course, dic, visited, parents):
        if course in parents:
            return False

        visited.add(course)
        parents.add(course)
        result = True
        if course in dic:

            for i in dic[course]:
                result = self.DFS(i, dic, visited, parents)
                if result == False:
                    break

        parents.remove(course)  # critical, in correspondence w add

        return result

        # option 1: BFS
        # if len(prerequisites) == 0:
        #     return True

        # in_degree = {}  # critical addtional data structure
        # for i in range(numCourses):
        #     in_degree[i] = 0

        # # translate to graph
        # dic = {}
        # for pair in prerequisites:
        #     course_number = pair[0]
        #     pre_course = pair[1]
        #     in_degree[course_number] += 1  # count in-degree/pre-requisites
        #     # remove course with prerequisite to cover course w/o pre-requisites into q

        #     self.add_precourse(course_number, pre_course, dic)

        # visited = set()

        # q = deque([])
        # for k in in_degree:
        #     if in_degree[k] == 0:  # critical,add only no in_degree/pre-requisits
        #         q.append(k)

        # while len(q) > 0:
        #     l = len(q)
        #     for _ in range(l):
        #         current = q.popleft()
        #         visited.add(current)  # visited
        #         if current not in dic:  # current may not in dic if no neighbors
        #             continue
        #         for next_course in dic[current]:
        #             in_degree[next_course] -= 1  # critical, reduce in_degree
        #             if in_degree[next_course] == 0:  # critical, add only when no in_degree
        #                 q.append(next_course)

        # if len(visited) == numCourses:
        #     return True  # when all courses are taken within numcourses
        # return False

        # [course_number/prerequisits:[next]]

    def add_precourse(self, course_number, pre_course, dic):
        if pre_course not in dic:
            dic[pre_course] = []

        dic[pre_course].append(course_number)
        # @lc code=end

    '''3\n[[1,0],[0,2],[1,2]] -->true
    3\n[[1,0],[0,2],[2,1]] -->false
    3\n[[0,1],[0,2],[1,2]]-->true
    4\n[[2,0],[1,0],[3,1],[3,2],[1,3]]-->false
    3\n[[1,0],[2,0]]-->true
    4\n[[1,0],[2,0],[3,1],[3,2]]-->true
    '''
