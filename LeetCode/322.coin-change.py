'''
You are given coins of different denominations and a total amount of money 
amount. Write a function to compute the fewest number of coins that you 
need to make up that amount. If that amount of money cannot be made up by 
any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2
 

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
'''
#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        # print(coins)
        result = []
        dic = {}

        self.recursive(coins, amount, [], result, dic)
        if len(result) == 0:
            return -1
        # print("result", result, dic)
        return min(result)

    def recursive(self, coins, amount, temp, result, dic):

        # print(coins, amount, temp, result)
        if amount == 0:
            result.append(len(temp))
            return

        if len(coins) == 0:
            return

        if amount < 0:
            return

        if amount in dic:
            return

        current = coins[0]
        count = 0
        l = amount // current
        # while count <= l:
        for i in range(l):
            temp.append(current)
            amount -= current

        while count < l:
            result_count = len(result)
            self.recursive(coins[1:], amount, temp, result, dic)
            if result_count != len(result):
                dic[amount] = min(result)

            temp.pop()
            amount += current
            count += 1

        self.recursive(coins[1:], amount, temp, result, dic)


# @lc code=end
