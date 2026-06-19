class Solution:
    def scoreOfString(self, s: str) -> int:
        a = 0
        for i in range(1,len(s)):
            j = i -1
            asc1 = ord(s[i])
            asc2 = ord(s[j])
            val = abs(asc1-asc2)
            a = a + val
        return a
