from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        INF = 2**31 - 1
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    queue.append((i,j))
        
        while queue:
            i, j = queue.popleft()
            for dx, dy in ((1, 0),(-1, 0),(0,1),(0,-1)):
                hor = i + dx
                ver = j + dy
                if hor >= 0 and hor < row and ver >= 0 and ver < col and grid[hor][ver] == INF:
                    grid[hor][ver] = grid[i][j] + 1
                    queue.append((hor, ver))

        
