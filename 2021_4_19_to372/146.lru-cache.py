#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = deque([])  # store queue for LRUC
        self.dic = {}  # store key value for O(1)

    def get(self, key: int) -> int:
        if key in self.dic:
            result = [key, self.dic[key]]
            self.q.remove(result)
            self.q.append(result)
            return result[1]  # return value not pair or key
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.dic:
            if len(self.q) >= self.capacity:
                least_used = self.q.popleft()
                del self.dic[least_used[0]]  # remember to delete dic as well
            self.q.append([key, value])
        else:
            self.queue([key, dic[key]]) = value  # how to update queue's value?
            self.dic[key] = value  # update value

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)

            # @lc code=end
