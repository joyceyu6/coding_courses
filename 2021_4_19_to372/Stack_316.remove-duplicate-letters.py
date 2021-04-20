'''
Given a string s, remove duplicate letters so that every letter appears once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.
'''

#
# @lc app=leetcode id=316 lang=python3
#
# [316] Remove Duplicate Letters
#

# @lc code=start


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occ = {c: i for i, c in enumerate(s)}
        stack = ["!"]
        Visited = set()

        for i, symbol in enumerate(s):
            if symbol in Visited:
                continue

            while (symbol < stack[-1] and last_occ[stack[-1]] > i):
                Visited.remove(stack.pop())

            stack.append(symbol)
            Visited.add(symbol)
        return "".join(stack)[1:]

# @lc code=end

# same as 1081


'''
build our answer in greedy way: we take letter by letter and put them into stack: 
if we have next letter which decreased lexicographical order of string, we remove it from 
stack and put new letter. 
However we need to be careful: if we remove some letter from stack and it was the last occurence, 
then we failed: we can not finish this process.
1. Find last_occ: last occurences for each letter in our string
2. Initialize our stack either as empty or with symbol, which is less than any letter ('!' in my case), 
so we do not need to deal with the case of empty stack. Also initialize Visited as empty set.
3. Iterate over our string and if we already have symbol in Visited, we just continue.
4. Then, we try to remove elements from the top of our stack: we do it, if new symbol is less than 
previous and also if last occurence of last symbol is more than i: it means that we have removed symbol 
later in our string, so if we remove it we will not fail to constract full string.
5. Append new symbol to our stack and mark it as visited.
6. Finally, return string built from our stack.
'''
