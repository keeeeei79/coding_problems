from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 隣の家には強盗に行けない
        # dpには自分まででの最大の値を入れる
        # dp[i]はdp[i-2]にnums[i]を足すかnums[i-1]か
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


s = Solution()
s.rob([2, 7, 9, 3, 1, 5])
