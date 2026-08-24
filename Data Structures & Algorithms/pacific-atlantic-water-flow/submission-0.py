class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        row = len(heights)
        col = len(heights[0])

        def dfs(r, c, hashmap, current_val):
            if r < 0 or r >= row or c < 0 or c >= col or current_val > heights[r][c] or (r, c) in hashmap:
                return
            current_val = heights[r][c]
            hashmap.add((r, c))
            dfs(r + 1, c, hashmap, current_val)
            dfs(r - 1, c, hashmap, current_val)
            dfs(r, c + 1, hashmap, current_val)
            dfs(r, c - 1, hashmap, current_val)
        
        for i in range(row):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, col - 1, atlantic, heights[i][col-1])
        
        for j in range(col):
            dfs(0, j, pacific, heights[0][j])
            dfs(row - 1, j, atlantic, heights[row - 1][j])
        
        results = []
        for i in range(row):
            for j in range(col):
                if (i, j) in pacific and (i, j) in atlantic:
                    results.append([i,j])
        return results


