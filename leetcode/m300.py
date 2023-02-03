from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n  # dp[i]はnums[0~i]までで最大の値
        for i in range(n):
            for j in range(i):  # iを固定したまま、0~i-1を動かす
                # nums[i] > nums[j]なら条件を満たす
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
