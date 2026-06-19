class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i <len(nums):
            if nums[i]==0:
                nums.pop(i)
                j = j + 1
            else:
                i = i + 1
        for k in range(j):
            nums.append(0)
