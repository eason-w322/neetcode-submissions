import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        queue = []
        x, y = points[0]
        heapq.heappush(queue,(0, x, y))
        visited = set()

        total_cost = 0

        while queue:
            cost, x1, y1 = heapq.heappop(queue)
            if (x1, y1) in visited:
                continue
            visited.add((x1, y1))
            total_cost += cost
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                if (x2, y2) in visited:
                    continue
                dist = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(queue, (dist, x2, y2))
        
        return total_cost

                
            
                

        
