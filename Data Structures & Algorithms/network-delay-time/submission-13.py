import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((t, v))
        dist = [float("inf")] * (n + 1)
        dist[k] = 0

        min_heap = []
        heapq.heappush(min_heap, (0, k))
        
        visited = set()
        while min_heap:
            cost, node = heapq.heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            for weight, neighbor in graph[node]:
                if dist[neighbor] > cost + weight:
                    dist[neighbor] = cost + weight
                    heapq.heappush(min_heap, (dist[neighbor], neighbor))
        
        dist = dist[1:]
        if any(i == float("inf") for i in dist):
            return -1
        return max(dist)




        
        


        