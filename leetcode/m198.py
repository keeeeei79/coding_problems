from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1つ新たに加えた時に、それを加えた場合の最大とそれを加えない場合の最大を比較して大きい方を取る
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_exclude_me = [0] * len(nums)
        for i in range(1, len(nums)):
            max_exclude_me[i] = dp[i - 1]
            dp[i] = max(max_exclude_me[i - 1] + nums[i], max_exclude_me[i])
        return dp[-1]


s = Solution()
s.rob([9, 1, 2, 9, 1])
