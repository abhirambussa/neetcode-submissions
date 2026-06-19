class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        k = len(nums1) - m
        for i in range(k):
            nums1.pop()
        i, j = 0, 0
        if len(nums1)==0:
            nums1.extend(nums2)
        else:
            while i < len(nums1) and j < len(nums2):
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    j = j + 1
                i = i + 1
            if j < len(nums2):
                nums1.extend(nums2[j:])