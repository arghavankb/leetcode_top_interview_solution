class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_strip = s.strip()
        s_split = s_strip.split(" ")

        return len(s_split[-1])
