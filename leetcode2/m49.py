from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            chars = [0] * 26
            for c in s:
                chars[ord(c) - ord("a")] += 1
            key = str(chars)
            if key in dic.keys():
                dic[key].append(s)
            else:
                dic[key] = [s]
        return dic.values()


s = Solution()
s.groupAnagrams(["bdddddddddd", "bbbbbbbbbbc"])
