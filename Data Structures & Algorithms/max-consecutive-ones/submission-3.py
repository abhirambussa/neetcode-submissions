class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        x = 0
        for i in range(len(nums)):
            
            if i == 0 and nums[i]==1:
                x = x + 1
            elif nums[i-1]==1 and nums[i]==1:
                x = x + 1
            elif nums[i-1]==1 and nums[i]==0:
                if ans<x:
                    ans = x
                x = 0
            elif nums[i-1]==0 and nums[i]==1:
                x = x + 1
        if x > ans:
            ans = x
        return ans
            


            
                