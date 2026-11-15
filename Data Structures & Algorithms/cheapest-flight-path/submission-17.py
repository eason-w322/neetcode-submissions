class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, p in flights:
            graph[u].append((p,v))
        
        dist = [float("inf")] * n
        dist[src] = 0

        queue = deque()
        queue.append((0, src))

        edges_remaining = k + 1

        while queue and edges_remaining:
            length = len(queue)
            for _ in range(length):
                cost, node = queue.popleft()
                for weight, neighbor in graph[node]:
                    if dist[neighbor] > cost + weight:
                        dist[neighbor] = cost + weight
                        queue.append((dist[neighbor], neighbor))
            edges_remaining -= 1

        if dist[dst] == float("inf"):
            return -1
        else:
            return dist[dst]



