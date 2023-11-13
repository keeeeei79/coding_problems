class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1":
                    res += 1
                    self.dfs(r, c, grid)
        return res

    def dfs(self, r: int, c: int, grid: List[List[str]]):
        if r < 0 or r >= len(grid):
            return
        if c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] != "1":
            return
        grid[r][c] = "#"
        self.dfs(r - 1, c, grid)
        self.dfs(r + 1, c, grid)
        self.dfs(r, c - 1, grid)
        self.dfs(r, c + 1, grid)
