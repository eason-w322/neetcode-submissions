class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for source, destination, price in flights:
            graph[source].append((price, destination))
        dist = [float("inf")] * n
        dist[src] = 0
        queue = deque()
        queue.append((0, src))
        t = k + 1

        while queue:
            if t == 0:
                break 
            t -= 1
            length = len(queue)
            for _ in range(length):

                cost, node = queue.popleft()
                for weight, neighbor in graph[node]:
                    if dist[neighbor] > cost + weight:
                        dist[neighbor] = cost + weight
                        queue.append((dist[neighbor], neighbor))
        
        
        if dist[dst] == float("inf"):
            return -1
        else:
            return dist[dst]





