class Solution:
    def firstUniqChar(self, s: str) -> int:
        se = set(s)
        d = dict()
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i] = d[i]+ 1

        for i in range(len(s)):
            if d[s[i]]==1:
                return i
        return -1