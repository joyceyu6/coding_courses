#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda item: item[0])  # sort with key

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        result = []
        for i in range(len(intervals)):

            current_start = intervals[i][0]
            current_end = intervals[i][1]

            if current_start > prev_end:
                result.append([prev_start, prev_end])
                prev_start = current_start
                prev_end = current_end

                continue
            prev_start = min(current_start, prev_start)
            prev_end = max(current_end, prev_end)

        # missing last one when out of loop
        result.append([prev_start, prev_end])
        return result

        # @lc code=end
