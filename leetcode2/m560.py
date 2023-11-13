from typing import List
from collections import defaultdict


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         output = []
#         for i in range(len(nums)):
#             self.dfs(nums[i + 1 :], k - nums[i], [i], output)
#         return len(output)

#     def dfs(self, nums: List[int], k: int, res: List[int], output: List[List[int]]):
#         if k == 0:
#             output.append(res)

#         if nums:
#             self.dfs(nums[1:], k - nums[0], res + [nums[0]], output)


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # iまでの合計とjまでの合計の差がkならsum(nums[i+1]~nums[j])=kになる
        # nums[j]について考えた時、過去にnums[j]-kの値を持つnums[i]が存在していればi+1~jの配列の合計がkになる
        d = defaultdict(int)
        d[0] = 1
        total = 0
        cnt = 0
        for n in nums:
            total += n
            cnt += d[total - k]
            d[total] += 1
        return cnt


s = Solution()
s.subarraySum([1, -1, 0], 2)
