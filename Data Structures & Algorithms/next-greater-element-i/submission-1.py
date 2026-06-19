class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = []
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    if j+1 < len(nums2):
                        l = False
                        for k in range(j+1,len(nums2)):
                            if nums2[j]<nums2[k]:
                                final.append(nums2[k])
                                l = True
                                break
                        if l == False:
                            final.append(-1)        
                    else:
                        final.append(-1)
        return final


                    