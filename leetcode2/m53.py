class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 自分が右端に含まれる形で最大の値を格納する
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)
