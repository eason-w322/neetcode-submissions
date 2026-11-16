class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        def dfs(r, c):
            nonlocal count
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0:
                return
            grid[r][c] = 0
            count += 1
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
            return count
        
        max_count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    count = 0
                    max_count = max(max_count, dfs(i, j))
        return max_count
                
        