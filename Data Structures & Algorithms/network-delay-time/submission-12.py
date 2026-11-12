import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        queue = []
        heapq.heappush(queue, (0, k))
        visited = set()

        while queue:
            t, u = heapq.heappop(queue)
            if u in visited:
                continue
            visited.add(u)

            for neighbor, time in graph[u]:
                if dist[neighbor] > t + time:
                    dist[neighbor] = t + time
                    heapq.heappush(queue, (dist[neighbor], neighbor))
        
        dist = dist[1:]
        if any(i == float("inf") for i in dist):
            return -1
        else:
            return max(dist)

        
        


        