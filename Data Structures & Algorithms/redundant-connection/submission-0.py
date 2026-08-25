class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = [i for i in range(n+1)]
        rank = [1] * (n + 1)

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 == p2:
                return False
            if rank[p1] >= rank[p2]:
                parents[p2] = p1
            else:
                parents[p1] = p2
            return True
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
