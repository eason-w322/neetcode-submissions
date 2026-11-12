import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float("inf") for _ in range(n + 1)]
        dist[k] = 0
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        queue = deque()
        queue.append((k, 0))
        visited = {}

        while queue:
            length = len(queue)
            for _ in range(length):
                u, t = queue.popleft()

                for neighbor, time in graph[u]:
                    if dist[neighbor] > t + time:
                        dist[neighbor] = t + time
                        queue.append((neighbor, dist[neighbor]))
        
        dist = dist[1:]
        if any(i == float("inf") for i in dist):
            return -1
        else:
            return max(dist)

        
        


        