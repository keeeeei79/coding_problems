from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        grid = [[None] * n for _ in range(m)]

        def dfs(i: int, j: int):
            if i >= m or j >= n or obstacleGrid[i][j]:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if not grid[i][j] is None:
                return grid[i][j]

            ans = dfs(i + 1, j) + dfs(i, j + 1)
            grid[i][j] = ans
            return ans

        return dfs(0, 0)


s = Solution()
s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
