class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)
            if p1 == p2:
                return False
            if rank[p1] <= rank[p2]:
                parent[p1] = p2
                rank[p1] += rank[p2]
            else:
                parent[p2] = p1
                rank[p2] += rank[p1]
            return True
        
        for x1, x2 in edges:
            if not union(x1, x2):
                return False
        return True

        


        
        