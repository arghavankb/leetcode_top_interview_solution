# First Solution
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_strip = s.strip()
        s_split = s_strip.split(" ")

        return len(s_split[-1])



# Second Solution
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         i = len(s)
#         l = 0
#
#         while i > 0:
#             i-=1
#             if s[i] != " ":
#                 l+=1
#             elif l!=0:
#                 break
#
#         return l
