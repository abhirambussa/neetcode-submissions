class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        total = sum(nums)

        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = sum(nums)-nums[i]
                if left==right:
                    return i
            else:
                left = left + nums[i-1]
                right = sum(nums)-left-nums[i]
                if left == right:
                    return i
        return -1