from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # iまでで最大のsubsequenceの長さを考える
        # iまででの最大になりうるケースは
        ## iとは関係なくi-1まででの最大 or iが入ったことで生まれるルートでの最大
        # iが入ったことで生まれるルートでの最大は
        ## 0~i-1までの最大+1
        # つまり iとは関係なくi-1まででの最大 or 0~i-1までの最大+1
        # よってi-1までの最大値と新しく加えたiがそこに加えられるかという情報を持てばいい
        # これをiを1つずつ大きくして計算する
        dp = [1] * len(nums)
        max_v = [0] * len(nums)
        sec_v = [0] * len(nums)
        max_v[0] = nums[0]
        for i in range(1, len(nums)):
            # nums[i]がdp[i-1]に足せるのかを判定する
            if max_v[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
                max_v[i] = nums[i]
                sec_v[i] = max_v[i - 1]
            else:
                dp[i] = dp[i - 1]
                # もしnums[i]を使ってもdp[i-1]と値が変わらないなら更新したい
                if sec_v[i - 1] < nums[i] < max_v[i - 1]:
                    max_v[i] = nums[i]
                else:
                    max_v[i] = max_v[i - 1]
                sec_v[i] = sec_v[i - 1]
        return dp[-1]


s = Solution()
s.lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
