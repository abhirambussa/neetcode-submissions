class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people)-1
        ans = 0
        while i <=j:
            if i < j:
                if people[i]+people[j]<= limit:
                    ans = ans + 1
                    i = i + 1
                    j = j - 1
                else:
                    if people[j]<= limit:
                        ans = ans + 1
                        j = j - 1
            else:
                ans = ans + 1
                return ans
        return ans

        