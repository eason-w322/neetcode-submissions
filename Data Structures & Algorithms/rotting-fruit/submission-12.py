from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
        t = 0
        visited = set()
        while queue:
            length = len(queue)
            rottened = False
            for _ in range(length):
                x, y = queue.popleft()
                if (x, y) in visited:
                    continue
                visited.add((x,y))
                for dx, dy in ((1,0), (-1, 0), (0, 1), (0, -1)):
                    r = x + dx
                    c = y + dy
                    if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 1:
                        continue
                    if (r, c) in visited:
                        continue
                    grid[r][c] = 2
                    queue.append((r,c))
                    rottened = True
            if rottened == True:
                t += 1
            
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        return t
        



