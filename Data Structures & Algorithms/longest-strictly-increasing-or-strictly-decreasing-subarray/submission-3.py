class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans1 = 1
        ans2 = 1
        t = 0
        s = 0
        x = 0
        y = 0
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                if t ==0:
                    x = 2
                    t = 1
                else:
                    x = x + 1
                if i+1 == len(nums)-1:
                    if x > ans1:
                        ans1 = x
            else: 
                if x > ans1:
                    ans1 = x
        
                x = 0
                t = 0
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                if s ==0:
                    y = 2
                    s = 1
                else:
                    y = y + 1
                if j+1 == len(nums)-1:
                    if y > ans2:
                        ans2 = y
            else: 
                if y > ans2:
                    ans2 = y
                y = 0
                s = 0

        return max(ans1,ans2)