class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a = {}
        for i in arr:
            if i in a:
                a[i]= a[i] + 1
            else:
                a[i] = 1
        arr = sorted(arr)
        for j in range(len(arr)-1,-1,-1):
            if a[arr[j]]==arr[j]:
                return arr[j]
        return -1
        