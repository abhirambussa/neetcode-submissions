class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a:
                a[i]= a[i]+1
            else:
                a[i]= 1
        max = 0
        value = -1
        s = set(nums)
        for i in s:
            if a[i]>max:
                max = a[i]
                value = i
        return value           
        