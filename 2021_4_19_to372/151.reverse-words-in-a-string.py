#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        # option 1: split, with extra memory though
        s_split = s.split(" ")
        result = []
        for i in range(len(s_split)-1, -1, -1):
            if s_split[i] == "":
                continue

            result.append(s_split[i])

        return " ".join(result)

        # option 2: in-place with constant memroy - need convert to list in Python

        # word_start = -1
        # word_end = -1
        # reversed_index = -1
        # index = 0
        # while index < len(s):
        #     print(index, reversed_index, s)
        #     if s[index] != " ":
        #         print(index, reversed_index, s, "start")
        #         word_start, word_end = index, index
        #         while word_end < len(s):  # find start and end of the non blank word
        #             if s[word_end] == " ":
        #                 break
        #             word_end += 1

        #         print(word_start, word_end)
        #         # reverse the word in place
        #         word_to_reverse = s[word_start:word_end+1]
        #         print(word_to_reverse, "word_to_reverse")
        #         reverse_word = word_to_reverse[::-1]
        #         print(reverse_word, "reversed word")

        #         # string is not mutable, how to replace?
        #         # from reversed_index + 1 to be replaced with reversed_word?
        #         # ......
        #         print(s)
        #         reversed_index = reversed_index+len(reverse_word)
        #         index = word_end + 1
        #         print(index, reversed_index, s, "end")
        #     index += 1
        # return s[reversed_index:-1:-1]

        # @lc code=end
:
