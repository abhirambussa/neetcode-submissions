class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        i = 0
        j = len(nums)-1
        def reverse( nums, a, b):
            while b > a:
                nums[a], nums[b] = nums[b], nums[a]
                a = a + 1
                b = b - 1
        reverse(nums, i, j)
        reverse(nums, i, k - 1)
        reverse(nums, k, len(nums) - 1)