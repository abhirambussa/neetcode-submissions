class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s)-1
        while i >= 0 and s[i]== " ":
            i = i - 1
        while i >= 0 and s[i]!= " ":
            length= length + 1
            i = i -1
        return length



        