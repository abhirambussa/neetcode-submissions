class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while i<j:
            v = s[i]
            s[i] = s[j]
            s[j] = v
            i = i + 1
            j = j - 1