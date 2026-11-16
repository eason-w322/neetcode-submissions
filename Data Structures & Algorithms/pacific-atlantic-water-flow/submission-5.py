class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(r, c, val, ocean):
            if r < 0 or r >= row or c < 0 or c >= col or heights[r][c] < val:
                return
            if (r, c) in ocean:
                return
            val = heights[r][c]
            ocean.add((r, c))
            dfs(r + 1, c, val, ocean)
            dfs(r - 1, c, val, ocean)
            dfs(r, c + 1, val, ocean)
            dfs(r, c - 1, val, ocean)
        
        for i in range(row):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i, col - 1, heights[i][col-1], atlantic)
        
        for j in range(col):
            dfs(0, j, heights[0][j], pacific)
            dfs(row - 1, j, heights[row-1][j], atlantic)
        
        results = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    results.append([i, j])
        
        return results
        
    
            

