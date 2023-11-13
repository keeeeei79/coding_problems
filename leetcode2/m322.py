from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 自分を何枚使ってもいい
        # dpでiを実現するのに最小の枚数を持っておく
        # dp[i] = min(dp[i], dp[i-total])
        # amountを下から計算していくことで既に自分を使った上での最小枚数がメモされている
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for x in range(coins[i], amount + 1):
                dp[x] = min(dp[x], dp[x - coins[i]] + 1)
        return dp[-1] if dp[-1] != float("inf") else -1


s = Solution()
# s.coinChange([1, 2, 5], 11)
s.coinChange([1], 0)
