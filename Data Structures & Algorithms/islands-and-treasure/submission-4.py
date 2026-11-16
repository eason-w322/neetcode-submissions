from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        INF = 2**31 - 1

        min_heap = []

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    heapq.heappush(min_heap, (0, i, j))

        visited = set()
        while min_heap:
            ###length = len(min_heap)
            ###for _ in range(length):
            time, r, c = heapq.heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r,c))
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x = r + dx
                y = c + dy
                if x < 0 or x >= row or y < 0 or y >= col or grid[x][y] == -1:
                    continue
                if (x, y) in visited:
                    continue
                if grid[x][y] == INF:
                    grid[x][y] = time + 1
                    heapq.heappush(min_heap, (grid[x][y], x, y))




        
