class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = len(strs[0])
        ans = ""
        for i in range(a):
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return ans
            
            ans = ans + strs[0][i]
        return ans
            


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                # ✅ fix: check length before accessing
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return ans
            
            ans += strs[0][i]
        
        return ans

        