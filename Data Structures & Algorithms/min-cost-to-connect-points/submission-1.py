import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        x, y = points[0]
        min_heap = []
        heapq.heappush(min_heap, (0, (x, y)))
        best = [float("inf")] * n
        visited = set()
        min_dist = 0
        
        while min_heap:
            cost, (xi, yi) = heapq.heappop(min_heap)
            if (xi, yi) in visited:
                continue
            visited.add((xi, yi))
            min_dist += cost

            for i in range(n):
                xj, yj = points[i]
                if (xj, yj) in visited:
                    continue
                dist = abs(xi - xj) + abs(yi - yj)
                if dist < best[i]:
                    best[i] = dist
                    heapq.heappush(min_heap,(dist,(xj, yj)))
        return min_dist

