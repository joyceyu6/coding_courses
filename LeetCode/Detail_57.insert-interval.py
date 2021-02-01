#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        # step 1: find where to insert; original intervals non-overlapping
        startCompareIndex = -1
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:  # critical, when to stop
                startCompareIndex = i
                break

        # if the last one
        if startCompareIndex == -1:
            intervals.append(newInterval)
            # cannot return intervals.append(newInterval) directly
            return intervals

        # merge if necessary
        result = intervals[:startCompareIndex]
        priorStart = newInterval[0]
        priorEnd = newInterval[1]
        while startCompareIndex <= len(intervals) - 1:

            currentStart = intervals[startCompareIndex][0]
            currentEnd = intervals[startCompareIndex][1]

            if currentStart > priorEnd:
                result.append([priorStart, priorEnd])
                result.extend(intervals[startCompareIndex:])  # extend
                return result  # return here if found

            priorStart = min(priorStart, currentStart)
            priorEnd = max(priorEnd, currentEnd)

            startCompareIndex += 1
        # if not found in the loop,append to the lst
        result.append([priorStart, priorEnd])
        return result

        # @lc code=end
