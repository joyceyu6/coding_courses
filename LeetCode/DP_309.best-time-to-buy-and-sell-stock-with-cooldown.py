'''
Say you have an array for which the ith element is the price
of a given stock on day i.

Design an algorithm to find the maximum profit. You may
complete as many transactions as you like (ie, buy one and
sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day.
(ie, cooldown 1 day)
'''
#
# @lc app=leetcode id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#

# @lc code=start


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        notHold, notHold_cooldown, hold = 0, float('-inf'), float('-inf')
        for p in prices:
            hold, notHold, notHold_cooldown = max(
                hold, notHold - p), max(notHold, notHold_cooldown), hold + p
        return max(notHold, notHold_cooldown)


# @lc code=end


'''
    The key is 3 states and 5 edges for state transition.
    3 states are notHold (stock), hold (stock), and notHold_cooldown.
    The initial values of the latter two are negative infinity since they
    are meaningless, i.e. you won't hold stocks at first and there's no
    cooldown at first. The 5 edges:

    (1) hold -----do nothing----->hold

    (3) hold -----sell----->notHold_cooldown

    (2) notHold -----do nothing -----> notHold

    (1) notHold -----buy-----> hold

    (2) notHold_cooldown -----do nothing----->notHold
'''
