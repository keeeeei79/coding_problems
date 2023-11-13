from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        ans = 0
        min_vals = [0] * n
        min_vals[0] = prices[0]
        for i in range(1, n):
            min_vals[i] = min(min_vals[i - 1], prices[i])
            ans = max(ans, prices[i] - min_vals[i])
        return ans


s = Solution()
s.maxProfit([7, 1, 5, 3, 6, 4])
