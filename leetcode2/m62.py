class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        queue = [(0, 0)]
        while queue:
            i, j = queue.pop(0)

            if not i == j == 0 and grid[i][j] != 0:
                continue

            if grid[i][j] == 0:
                upper = grid[i - 1][j] if 0 < i < m else 0
                left = grid[i][j - 1] if 0 < j < n else 0
                grid[i][j] = upper + left

            if i < m - 1:
                queue.append((i + 1, j))
            if j < n - 1:
                queue.append((i, j + 1))

        return grid[m - 1][n - 1]


s = Solution()
s.uniquePaths(3, 2)
