class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(0, len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for x1, x2 in edges:
            if not union(x1, x2):
                return [x1, x2]



