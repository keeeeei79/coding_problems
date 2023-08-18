class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sidx = 0
        for c in t:
            if len(s) == sidx:
                return True
            if c == s[sidx]:
                sidx += 1
        return len(s) == sidx
