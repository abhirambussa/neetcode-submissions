class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        
        i = 0
        j = 0

        while i < len(word) and j < len(abbr):

            # Case 1: letters match
            if word[i] == abbr[j]:
                i += 1
                j += 1

            else:

                # if current char is letter but not matching
                if abbr[j] >= "a" and abbr[j] <= "z":
                    return False

                # leading zero invalid
                if abbr[j] == '0':
                    return False

                c = 0

                # build full number
                while j < len(abbr) and abbr[j].isdigit():
                    c = c * 10 + int(abbr[j])
                    j += 1

                # skip characters in word
                i = i + c

        return i == len(word) and j == len(abbr)