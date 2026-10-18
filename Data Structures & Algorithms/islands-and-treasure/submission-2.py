from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        INF = 2**31 - 1

        queue = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    heapq.heappush(queue, (grid[i][j], i, j))
        
        while queue:
            dist, r, c = heapq.heappop(queue)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                hor, ver = r + dx, c + dy
                if hor < 0 or hor >= row or ver < 0 or ver >= col or grid[hor][ver] == -1:
                    continue
                if grid[hor][ver] > dist + 1:
                    grid[hor][ver] = dist + 1
                    heapq.heappush(queue, (grid[hor][ver], hor, ver))
   
                    


        
