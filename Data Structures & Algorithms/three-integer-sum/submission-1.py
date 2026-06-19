class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = list()
        for i in range(len(nums)-2):
            if i > 0 and nums[i]== nums[i-1]:
                continue
            else:
                j = i + 1
                k = len(nums)-1
                while j < k:
                    if j > i + 1 and nums[j]== nums[j -1]:
                        j = j + 1
                    elif k < len(nums)-1 and nums[k]== nums[k+ 1]:
                        k = k -1
                    else:
                        if nums[j]+nums[k]== -nums[i]:
                            result.append([nums[i], nums[j], nums[k]])
                            j = j + 1
                            k = k -1
                        elif nums[j]+nums[k]> -nums[i]:
                            k = k -1
                        elif nums[j]+nums[k]< -nums[i]:
                            j = j + 1
        return result
                    