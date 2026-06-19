class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    ans.add(i)
                    break
        unique_list = list(set(ans))
        return list(ans)

        
                
