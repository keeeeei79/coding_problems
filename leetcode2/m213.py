class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[0]を使うケースでは必ずnums[1]とnums[-1]が使われていない
        # なのでこれはnums[0]を使うケースのmaxはnums[:-1]に対する結果以下になる
        # 一方でnums[0]を使わないケースのmaxはnums[1:]に対する結果以下になる
        if len(nums) < 2:
            return nums[0]
        return max(self.simpleRob(nums[1:]), self.simpleRob(nums[:-1]))

    def simpleRob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]
