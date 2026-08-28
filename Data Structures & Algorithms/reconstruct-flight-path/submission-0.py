class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for u, v in tickets:
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
        for u in graph:
            graph[u].sort(reverse = True)
        
        results = []
        def dfs(node):
            while graph.get(node, []):
                next_node = graph[node].pop()
                dfs(next_node)
            results.append(node)
        
        dfs("JFK")
        return results[::-1]




