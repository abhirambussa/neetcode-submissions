class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ch = dict()
        l = set()
        for i in range(len(s)):
            if s[i] not in ch:
                if t[i] in l:
                    return False
                else:
                    ch[s[i]]= t[i]
                    l.add(t[i])
            else:
                if ch[s[i]]!= t[i]:
                    return False
        return True