from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        time = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j, time))
        
        while queue:
            length = len(queue)
            for _ in range(length):
                i, j, time = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1),(0, -1)):
                    hor = i + dx
                    ver = j + dy
                    if hor < 0 or hor >= row or ver < 0 or ver >= col or grid[hor][ver] == 0:
                        continue
                    if grid[hor][ver] == 1:
                        grid[hor][ver] = 2
                        queue.append((hor, ver, time + 1))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        
        return time
    



