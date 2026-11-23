class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependency = defaultdict(list)
        for a, b in prerequisites:
            dependency[a].append(b)
        
        visiting = set()
        visited = set()
        results = []
        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for neighbor in dependency[node]:
                if not dfs(neighbor):
                    return False
            
            visiting.discard(node)
            visited.add(node)
            results.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return results
        
