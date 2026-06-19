class Solution:
    def maxDifference(self, s: str) -> int:
        oddmax = -1
        evenmin = len(s)+1
        link = dict()
        for i in s:
            if i in link:
                link[i] = link[i]+1
            else:
                link[i]= 1
            
        for i in s:
            if link[i]%2==0 and link[i]< evenmin:
                evenmin = link[i]
            if link[i]%2==1 and link[i]> oddmax:
                oddmax = link[i]
        return oddmax-evenmin