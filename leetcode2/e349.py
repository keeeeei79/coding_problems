class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        res = []
        for n in nums1:
            dic[n] = 1
        for n in nums2:
            if n in dic.keys():
                dic[n] += 1
        return [k for k, v in dic.items() if v > 1]
