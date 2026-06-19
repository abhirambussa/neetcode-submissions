class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ""
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1) and j < len(word2):
                word3 = word3 + word1[i]+ word2[j]
                i = i + 1
                j = j + 1
            if i < len(word1) and j >= len(word2):
                word3 = word3 + word1[i:]
                break
            if i >= len(word1) and j < len(word2):
                word3 = word3 + word2[j:]
                break
        return word3