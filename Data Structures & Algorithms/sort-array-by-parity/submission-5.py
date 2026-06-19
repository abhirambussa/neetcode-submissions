class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        if len(nums)==1:
            return nums
        i = 0
        j = 1
        while i < len(nums) and j < len(nums):
            if nums[i]%2==1 and nums[j]%2==1:
                j = j + 1
            elif nums[i]%2==1 and nums[j]%2==0:
                nums[i], nums[j] = nums[j], nums[i]
                i = i + 1
                j = j + 1
            elif nums[i]%2==0 and nums[j]%2==1:
                i = i + 1
                j = j + 1
            elif nums[i]%2==0 and nums[j]%2==0:
                if i == j:
                    i = i + 1
                    j = j + 1
                else:
                    i = i + 1
        return nums
        
                    

