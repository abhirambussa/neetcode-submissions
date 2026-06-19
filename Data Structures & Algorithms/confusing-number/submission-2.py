class Solution:
    def confusingNumber(self, n: int) -> bool:
        l = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        n = str(n)
        a = ""
        for i in reversed(n):
            if i in l:
                a = a + l[i]
            else:
                return False
        a = int(a)
        n = int(n)
        if a == n:
            return False
        else:
            return True
