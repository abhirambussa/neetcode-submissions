class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        test = dict()
        ans = set(nums)
        for i in nums:
            if i in test:
                ans.discard(i)
            else:
                test[i]= 1
        if len(ans)==0:
            return -1
        return max(ans)