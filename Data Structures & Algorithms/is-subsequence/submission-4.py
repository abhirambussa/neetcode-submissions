class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if len(s) == 0:
            return True
        else:
            for i in range(len(t)):
                if s[j]== t[i]:
                    j = j + 1
                    if j == len(s):
                        break
            if j == len(s):
                return True
            else:
                return False
        

        