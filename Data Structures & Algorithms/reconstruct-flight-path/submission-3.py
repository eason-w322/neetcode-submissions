class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)
        for airport in graph:
            graph[airport].sort(reverse = True)
        results = []
        
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
            results.append(node)
        
        dfs("JFK")
        return results[::-1]
            
        




