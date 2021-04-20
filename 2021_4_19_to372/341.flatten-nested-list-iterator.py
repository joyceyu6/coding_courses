#
# @lc app=leetcode id=341 lang=python3
#
# [341] Flatten Nested List Iterator
#

# @lc code=start
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.output = self.removeNestings(nestedList)
        self.current_index = 0
        # print(self.output)

    def next(self) -> int:
        if self.current_index < len(self.nestedList):
            self.current_index += 1
            return self.output[self.current_index]

    def hasNext(self) -> bool:
        self.prior_index = self.current_index
        if type(self.next) == 'int':
            self.current_index = self.prior_index
            return True
        return False

    def removeNestings(self, nestedList):
        output = []

        for i in nestedList:
            if type(i) == list:
                self.removeNestings(i)
            else:
                output.append(i)
        return output


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# @lc code=end
