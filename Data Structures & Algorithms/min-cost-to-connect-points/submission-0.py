import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        min_heap = []
        xi, yi = points[0]
        heapq.heappush(min_heap,(0, (xi, yi)))
        visited = set()
        best = [float("inf")] * n
        min_cost = 0
        

        while min_heap:
            cost, (x, y) = heapq.heappop(min_heap)
            if (x, y) in visited:
                continue
            visited.add((x, y))
            min_cost += cost

            for i in range(n):
                xj, yj = points[i]
                if (xj, yj) in visited:
                    continue
                dist = abs(x - xj) + abs(y - yj)
                if dist < best[i]:
                    best[i] = dist
                    heapq.heappush(min_heap, (dist, (xj, yj)))
        return min_cost
