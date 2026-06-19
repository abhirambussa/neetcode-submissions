class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        ch = dict()
        odd = set()
        for i in s:
            if i not in ch:
                ch[i]= 1
            else:
                ch[i] = ch[i] + 1
        for i in s:
            if ch[i]%2==1:
                odd.add(i)
        if len(s)%2==0 and len(odd)>0:
            return False
        elif len(s)%2==0 and len(odd)==0:
            return True
        elif len(s)%2==1 and len(odd)==1:
            return True
        else:
            return False

