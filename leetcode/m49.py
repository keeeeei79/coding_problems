class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            c = [0] * 26
            for x in s:
                c[ord(x) - ord("a")] += 1
            d[tuple(c)].append(s)
        return d.values()
