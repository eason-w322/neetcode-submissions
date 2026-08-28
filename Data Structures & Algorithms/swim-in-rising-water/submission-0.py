from collections import deque
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        min_heap = []
        heapq.heappush(min_heap, (grid[0][0],0,0))
        t = 0
        visited = set()
        visited.add((0,0))

        while min_heap:
                h, x, y = heapq.heappop(min_heap)
                t = max(t, h)
                if x == row - 1 and y == col - 1:
                    return t
                
                for dx, dy in ((1,0), (-1,0), (0,1), (0,-1)):
                    xi = x + dx
                    yi = y + dy
                    if xi >= 0 and xi < row and yi >= 0 and yi < col and (xi, yi) not in visited:
                        heapq.heappush(min_heap, (grid[xi][yi], xi, yi))
                        visited.add((xi, yi))
            





