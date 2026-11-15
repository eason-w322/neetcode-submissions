from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        queue = []
        heapq.heappush(queue, (grid[0][0], 0, 0))

        time = 0
        visited = set()
        while queue:
            h, x, y = heapq.heappop(queue)
            time = max(h, time)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            if x == row - 1 and y == col - 1:
                return time
            
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                hor = x + dx
                ver = y + dy
                if hor < 0 or hor >= row or ver < 0 or ver >= col:
                    continue
                if (hor, ver) in visited:
                    continue
                heapq.heappush(queue, (grid[hor][ver], hor, ver))







