from typing import List

# class Solution:
#     def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
#         m = len(obstacleGrid)
#         n = len(obstacleGrid[0])
#         dp = [[1] * n for _ in range(m)]
#         for i in range(m):
#             for j in range(n):
#                 if obstacleGrid[i][j]:
#                     dp[i][j] = 0
#                 elif i == 0 and j == 0:
#                     dp[i][j] = 1
#                 else:
#                     left = 0 if i < 1 or obstacleGrid[i - 1][j] else dp[i - 1][j]
#                     upper = 0 if j < 1 or obstacleGrid[i][j - 1] else dp[i][j - 1]
#                     dp[i][j] = left + upper
#         return dp[-1][-1]


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[None] * n for _ in range(m)]

        def dfs(i: int, j: int) -> int:
            if i >= m or j >= n:
                return 0
            if obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if not dp[i][j] is None:
                return dp[i][j]
            dp[i][j] = dfs(i + 1, j) + dfs(i, j + 1)  # down + right
            return dp[i][j]

        return dfs(0, 0)


s = Solution()
print(
    s.uniquePathsWithObstacles(
        [[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
    )
)
