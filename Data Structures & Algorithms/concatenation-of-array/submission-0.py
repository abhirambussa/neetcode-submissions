class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        out = nums
        for i in range(len(nums)):
            out.append(nums[i])
        return out
        