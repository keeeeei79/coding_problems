from typing import List, Union

# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         dp = [[1] * n for _ in range(m)]
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
#         return dp[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp: List[List[Union[int, None]]] = [[None] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if dp[i][j]:
                return dp[i][j]
            ans = dfs(i + 1, j) + dfs(i, j + 1)  # 右下から左上に進むと仮定している
            dp[i][j] = ans
            return ans

        return dfs(0, 0)


# [10, 6, 3, 1]
# [4, 3, 2, 1]
# [1, 1, 1, 1]

s = Solution()
s.uniquePaths(3, 4)
