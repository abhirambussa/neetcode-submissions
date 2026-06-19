class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""

        # Step 1: Add characters based on order
        for ch in order:
            for c in s:
                if c == ch:
                    ans += c

        # Step 2: Add remaining characters (not in order)
        for c in s:
            if c not in order:
                ans += c

        return ans