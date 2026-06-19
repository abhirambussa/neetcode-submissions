class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        ans = 0
        while i<j:
            if heights[i]> heights[j]:
                a = (j-i)*heights[j]
                j = j - 1
            else:
                a = (j-i)*heights[i]
                i = i + 1
            if a > ans:
                ans = a
        return ans
            