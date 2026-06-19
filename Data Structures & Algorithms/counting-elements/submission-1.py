class Solution:
    def countElements(self, arr: List[int]) -> int:
        s = set(arr)
        t = list()
        for i in arr:
            if i+1 in s:
                t.append(i)
        return len(t)