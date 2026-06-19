class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        j = 0
        for i in s:
            if j<len(t) and i == t[j]:
                j = j + 1
        if j == len(t):
            return 0
        else:
            return len(t)-j
