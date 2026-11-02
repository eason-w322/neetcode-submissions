import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        min_heap = []
        x, y = points[0]
        heapq.heappush(min_heap, (0, x, y))
        seen = set()

        total_cost = 0
        while min_heap:
            cost, xi, yi = heapq.heappop(min_heap)
            if (xi, yi) in seen:
                continue
            seen.add((xi, yi))
            total_cost += cost

            for xj, yj in points:
                if (xj, yj) in seen:
                    continue
                weight = abs(xi - xj) + abs(yi - yj)
                heapq.heappush(min_heap, (weight, xj, yj))
                

        return total_cost
        
            
                

        
