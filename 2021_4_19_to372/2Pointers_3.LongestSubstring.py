'''
3. Longest Substring Without Repeating Characters (Medium)
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:  # corner case
            return 1

        left = 0
        unique_set = set()
        longest = 0
        for right in range(len(s)):
            current = s[right]
            if current not in unique_set:
                unique_set.add(current)
            else:
                start = left
                for left in range(start, right):
                    unique_set.remove(s[left])  # remove s[left] not current
                    if current not in unique_set:
                        unique_set.add(current)
                        left += 1  # critical
                        break  # critial, to move right to the righter

            # okay to do it after if/else:
            longest = max(longest, len(unique_set))

        return longest


solution = Solution()
print(solution.lengthOfLongestSubstring("pwwkew"))
