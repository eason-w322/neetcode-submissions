import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        edges = {}
        for u, v, t in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v, t))
        
        min_heap = []
        heapq.heappush(min_heap, (dist[k], k))
        while min_heap:
            distance, u = heapq.heappop(min_heap)
            if distance > dist[u]:
                continue
            if u in edges:
                for v, t in edges[u]:
                    if dist[v] > distance + t:
                        dist[v] = distance + t
                        heapq.heappush(min_heap, (dist[v], v))
        
        if any(dist[i] == float("inf") for i in range(1, n + 1)):
            return -1
        else:
            return max(dist[1:])


        