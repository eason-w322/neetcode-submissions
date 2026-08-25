from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        row = len(grid)
        col = len(grid[0])

        queue = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        while queue:
            length = len(queue)
            rotted_this_level = False
            for _ in range(length):
                i, j = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    hor = i + dx
                    ver = j + dy
                    if hor >= 0 and hor < row and ver >= 0 and ver < col and grid[hor][ver] == 1:
                        grid[hor][ver] = 2
                        queue.append((hor, ver))
                        rotted_this_level = True
            if rotted_this_level:
                time += 1

        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1
        
        return time


