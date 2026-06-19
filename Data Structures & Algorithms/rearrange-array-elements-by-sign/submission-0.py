class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        flag = 1
        ans = []
        i, j = 0, 0
        while len(ans)< len(nums):
            if flag == 1:
                if nums[i]> 0:
                    ans.append(nums[i])
                    flag = 0
                    i = i + 1
                else:
                    i = i + 1
            else:
                if nums[j] < 0:
                    ans.append(nums[j])
                    flag = 1
                    j = j + 1
                else:
                    j = j + 1
        return ans