class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = dict()
        for i in nums:
            if i not in x:
                x[i]= 1
            else:
                x[i]= x[i] + 1
        asc = list(sorted(x.items(), key=lambda item: item[1], reverse = True))
        ans = []
        for i in range(k):
            ans.append(asc[i][0])

        return ans