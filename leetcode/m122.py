from typing import List


# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         # とりあえずbrute force
#         # TLE
#         n = len(prices)
#         return self.maxProfitFromK(prices, 0, n)

#     def maxProfitFromK(self, prices: List[int], k: int, n: int) -> int:
#         max_profit = 0
#         for i in range(k, n):
#             for j in range(i + 1, n):
#                 if prices[i] < prices[j]:
#                     profit = (prices[j] - prices[i]) + self.maxProfitFromK(
#                         prices, j + 1, n
#                     )
#                     max_profit = max(max_profit, profit)
#         return max_profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = prices[0]
        total = 0
        for i in range(1, len(prices)):
            if prices[i] < p:
                p = prices[i]
            elif prices[i] > p:
                total += prices[i] - p
                p = prices[i]
        return total


s = Solution()
s.maxProfit([7, 6, 4, 3, 1])
