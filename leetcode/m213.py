class Solution:
    def simple_rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        max_exclude_me_and_first = [0] * len(nums)
        for i in range(1, len(nums)):
            max_exclude_me_and_first[i] = dp[i - 1]
            dp[i] = max(max_exclude_me_and_first[i - 1] + nums[i], dp[i - 1])
        return dp[-1]

    def rob(self, nums: List[int]) -> int:
        # nums[1:]についてrobを行う
        # nums[1:]を超える可能性があるものはnums[1:]の最大にnums[0]を足したもの
        # nums[0]を足せるということはnums[1]とnums[-1]を使っていないということ
        # それはnums[:-1]についてrobを行なった結果と同じになるはず
        # なのでnums[1:]とnums[:-1]のそれぞれの結果をmaxする
        if len(nums) < 2:
            return nums[0]
        return max(self.simple_rob(nums[1:]), self.simple_rob(nums[:-1]))
