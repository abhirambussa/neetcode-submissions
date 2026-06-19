class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        def maximum(a):
            max = -1
            if a == len(arr):
                return -1
            else:
                for i in range(a+1, len(arr)):
                    if max < arr[i]:
                        max = arr[i]
                return max
        for j in range(len(arr)):
            arr[j]= maximum(j)
        return arr

            
        