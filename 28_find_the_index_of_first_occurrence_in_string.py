class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)

        i = 0
        while i <= (needle_length + haystack_length):
            if haystack[i:(i + needle_length)] == needle:
                return i
            else:
                i += 1

        return -1
