class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = -1
        y = ""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                x = int(num[i:i+3])
                if ans<x:
                    ans = x
                    y = num[i:i+3]
        return y
        