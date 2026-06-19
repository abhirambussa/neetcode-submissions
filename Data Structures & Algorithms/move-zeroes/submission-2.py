class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while j < len(nums):
            if i == j:
                j = j + 1
            else:
                if nums[j]!=0 and nums[i]==0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i = i + 1
                    j = j + 1

                elif nums[j]==0 and nums[i]==0:
                    j = j + 1

                elif nums[i]!= 0:
                    i = i + 1
