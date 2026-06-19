class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ver = []
        for i in range(1,len(nums)+1):
            ver.append(i)
        for i in range(len(nums)):
            if nums[i] in ver:
                ver.remove(nums[i])
        return ver


        