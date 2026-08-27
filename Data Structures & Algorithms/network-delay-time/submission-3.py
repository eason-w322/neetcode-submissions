import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf")] * (n + 1)
        graph = {}
        for u, v, t in times:
            if u not in graph:
                graph[u] = []
            graph[u].append((t, v))
        
        min_heap = []
        heapq.heappush(min_heap, (0, k))
        visited = set()
        dist[k] = 0

        while min_heap:
            distance, u = heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)

            for (t, v) in graph.get(u, []):
                if distance + t < dist[v]:
                    dist[v] = distance + t
                    heapq.heappush(min_heap, (dist[v], v))
        
        min_time = 0
        for i in range(1, n + 1):
            if dist[i] == float("inf"):
                return -1
            min_time = max(min_time, dist[i])
        return min_time



        