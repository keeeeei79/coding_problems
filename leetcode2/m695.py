class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                max_count = max(max_count, self.dfs(r, c, grid))
        return max_count

    def dfs(self, r: int, c: int, grid: List[List[int]]) -> int:
        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] != 1:
            return 0

        grid[r][c] = -1
        count = 1
        count += self.dfs(r - 1, c, grid)
        count += self.dfs(r + 1, c, grid)
        count += self.dfs(r, c - 1, grid)
        count += self.dfs(r, c + 1, grid)
        return count
