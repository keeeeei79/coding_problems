from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # iを加えた時に最大を更新するかの判定条件が複雑で難しい
        # ある程度全走査で最大を更新するかの判定を行うのが良さそう

        # dpはiまでのうちで最大の長さではなく、nums[i]が最大になるものの中で最大の長さを持つ
        # Let dp[i] is the longest increase subsequence of nums[0..i]
        # which has nums[i] as the end element of the subsequence.
        dp = [1] * len(nums)
        for i in range(len(nums)):
            # 自分より小さい数の過去のdpの最大+1を自分の長さとする
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()
s.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
