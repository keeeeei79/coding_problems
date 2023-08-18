from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i, n in enumerate(nums):
            lis = [n]
            ll = self.permute(nums=nums[:i] + nums[i + 1 :])
            if ll:
                for l in ll:
                    res.append(lis + l)
            else:
                res.append(lis)
        return res


s = Solution()
s.permute([1, 2, 3])
