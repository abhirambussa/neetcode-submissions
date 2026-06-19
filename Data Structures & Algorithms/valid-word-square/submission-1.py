class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        j = 0
        for i in range(len(words)):
            x = words[i]
            t = ""
            for m in words:
                if i < len(m):
                    t = t + m[i]
            if x == t:
                j = j +1
        if j == len(words):
            return True
        else:
            return False