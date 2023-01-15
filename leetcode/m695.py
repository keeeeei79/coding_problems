class Solution:
    def dfs(self, grid: List[List[int]], i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = -1
        count = 1
        count += self.dfs(grid, i - 1, j)
        count += self.dfs(grid, i + 1, j)
        count += self.dfs(grid, i, j - 1)
        count += self.dfs(grid, i, j + 1)
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count = self.dfs(grid, i, j)
                    if max_count < count:
                        max_count = count
        return max_count
