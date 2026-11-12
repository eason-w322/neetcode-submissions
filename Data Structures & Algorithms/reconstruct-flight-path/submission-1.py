class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        airport = set()
        for source, destination in tickets:
            graph[source].append(destination)
        for airpot in graph:
            graph[airpot].sort(reverse = True)

        path = []
        def dfs(node):
            while graph.get(node, []):
                next_node = graph[node].pop()
                dfs(next_node)
            path.append(node)
        
        dfs("JFK")
        return path[::-1]
            





