'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the 
number is. When your friend makes a guess, you provide a hint with the 
following info:

The number of "bulls", which are digits in the guess that are in the 
correct position.
The number of "cows", which are digits in the guess that are in your 
secret number but are located in the wrong position. Specifically, 
the non-bull digits in the guess that could be rearranged such that 
they become bulls.
Given the secret number secret and your friend's guess guess, return 
the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls 
and y is the number of cows. Note that both secret and guess may contain 
duplicate digits.
'''
#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#

# @lc code=start


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dic = {}
        a = 0
        b = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1
                continue  # skip process to be repeated

            if secret[i] not in dic:
                dic[secret[i]] = 1
            else:
                dic[secret[i]] += 1

        for j in range(len(guess)):
            if guess[j] == secret[j]:
                continue  # repeat needed, e.g. "11" "10"
            if guess[j] in dic and dic[guess[j]] > 0:
                b += 1
                dic[guess[j]] -= 1

        return str(a) + "A" + str(b) + "B"

        # @lc code=end
