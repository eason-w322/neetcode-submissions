class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(i, j, ocean, val):
            if i < 0 or i >= row or j < 0 or j >= col or (i, j) in ocean or heights[i][j] < val:
                return
            
            ocean.add((i,j))
            val = heights[i][j]
            dfs(i + 1, j, ocean, val)
            dfs(i - 1, j, ocean, val)
            dfs(i, j + 1, ocean, val)
            dfs(i, j - 1, ocean, val)
        
        for j in range(col):
            dfs(0, j, pacific, -float("inf"))
        for i in range(row):
            dfs(i, 0, pacific,  -float("inf"))
        
        for i in range(row):
            dfs(i, col-1, atlantic,  -float("inf"))
        for j in range(col):
            dfs(row-1, j, atlantic,  -float("inf"))
        
        results = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    results.append([i, j])
        
        return results
            

