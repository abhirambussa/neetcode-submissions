class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        ans = 0 
        j = 0
        for i in word:
            ans = ans + abs(keyboard.index(i)-j)
            j = keyboard.index(i)
        return ans