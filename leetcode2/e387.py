class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            if c in dic.keys():
                dic[c] += 1
            else:
                dic[c] = 1
        for i, c in enumerate(s):
            if dic[c] == 1:
                return i
        return -1
