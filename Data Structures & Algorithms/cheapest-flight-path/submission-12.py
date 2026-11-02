class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float("inf") for _ in range(n)]
        weights = {}
        for u, v, p in flights:
            if u not in weights:
                weights[u] = []
            weights[u].append((p, v))
        dist[src] = 0
        queue = deque()
        queue.append((0, src))
        edges_remaining = k + 1

        while queue and edges_remaining:
            length = len(queue)
            for _ in range(length):
                cost, u = queue.popleft()
                if u in weights:
                    for price, v in weights[u]:
                        if dist[v] > cost + price:
                            dist[v] = cost + price
                            queue.append((dist[v], v))
            edges_remaining -= 1

        return dist[dst] if dist[dst] != float("inf") else -1
                

