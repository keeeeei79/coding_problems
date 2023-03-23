class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                # coinを複数枚使えるが、2枚使う時でも"dp[x - coin]"は
                # 既にcoinを使った状態での値になるため単純に使う枚数は"dp[x - coin] + 1"でよい
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[-1] if dp[-1] != float("inf") else 0
