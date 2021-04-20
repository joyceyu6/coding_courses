#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        from collections import deque
        q = deque([])
        new_path = path.split("/")  # easier to split first

        for c in new_path:
            if c == "" or c == ".":
                continue

            if c == "..":
                if len(q) > 0:
                    q.pop()

            else:
                q.append(c)

        result = ""
        while len(q) > 0:
            current = q.popleft()  # critical: pop left first
            result += "/"
            result += current
            print(result)

        if len(result) == 0:
            result = "/"

        return result


# @lc code=end
