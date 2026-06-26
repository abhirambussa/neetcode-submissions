class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i , j = 0, 0
        count = 0
        a = 0
        while j< len(nums) and i < len(nums):
            if nums[i]== nums[j]:
                if count == 0:
                    count = count + 1
                    a = a + 1
                    j = j + 1
                elif count == 1:
                    count = count + 1
                    a = a + 1
                    j = j + 1
                elif count >= 2:
                    nums[j]== "_"
                    nums.pop(j)
                    nums.append("_")
            else:
                if nums[j]!= "_":
                    i = j
                    count = 0
                else:
                    return a
        return a

                
                

            

