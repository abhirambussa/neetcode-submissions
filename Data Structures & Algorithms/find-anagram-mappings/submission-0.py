class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1]*len(nums1)
        numd = dict()
        for i in range(len(nums2)):
            numd[nums2[i]]= i
        for j in range(len(nums1)):
            ans[j] = numd[nums1[j]]
        return ans