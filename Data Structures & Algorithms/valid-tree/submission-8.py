class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parents = [i for i in range(n)]
        indegree = [0] * n

        def find(x):
            while x != parents[x]:
                x = find(parents[x])
            return x
        
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)
            if p1 == p2:
                return False
            if indegree[p1] >= indegree[p2]:
                parents[p2] = p1
                indegree[p1] += indegree[p2]
            else:
                parents[p1] = p2
                indegree[p2] += indegree[p1]
            return True
        
        for x1, x2 in edges:
            if not union(x1, x2):
                return False
        
        return True


        


        
        