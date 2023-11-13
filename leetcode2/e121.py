class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i]を追加したときに値が更新されるパターンは
        # prices[i]が過去の最高を超えた時
        # なので最小の値をずっと持っておいて、それと自分の差を計算して最大のものを返す
        min_v = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            min_v = min(min_v, prices[i])
            max_profit = max(max_profit, prices[i] - min_v)
        return max_profit
