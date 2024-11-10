# First Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str :
        if not strs:
            return ""

        prefix = strs[0]

        for str in strs[1:]:
            while not str.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


# Second Solution
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str :
#         prefix = ""
#         for l in range(1, len(strs[0])+1):
#             searching_for = strs[0][0:l]
#             for str in strs[1:]:
#                 if len(str) < l or str[0:l] != searching_for:
#                     return prefix
#
#             prefix = searching_for
#         return prefix


