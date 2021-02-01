'''
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
'''

#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net_gas = []
        for i in range(len(gas)):
            net_gas.append(gas[i] - cost[i])

        start = 0
        while start < len(gas):
            if net_gas[start] < 0:
                start += 1
                continue

            sum_gas = 0
            end = start
            while sum_gas >= 0:
                index = end % len(gas)  # circle
                sum_gas += net_gas[index]

                if sum_gas < 0:
                    break

                end += 1
                if end == start + len(gas):
                    return start

            start = end + 1  # Greedy - skip all till end + 1

        return -1

        # @lc code=end
