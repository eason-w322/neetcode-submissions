from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        t = 0
        row = len(grid)
        col = len(grid[0])

        queue = []
        heapq.heappush(queue, (grid[0][0],0,0))

        t = 0
        visited = set()
        visited.add((0,0))
        while queue:
            h, x, y = heapq.heappop(queue)
            t = max(t, h)
            if x == row - 1 and y == col - 1:
                return t
            
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0,-1)):
                hor = x + dx
                ver = y + dy
                if hor < 0 or hor >= row or ver < 0 or ver >= col:
                    continue
                if (hor, ver) in visited:
                    continue
                visited.add((hor, ver))
                heapq.heappush(queue, (grid[hor][ver], hor, ver))

            
                    






