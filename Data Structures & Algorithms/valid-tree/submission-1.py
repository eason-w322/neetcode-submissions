class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        
        parents = [i for i in range(n)]
        rank = [1] * n
        count = n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)
            if p1 == p2:
                return False
            
            if rank[p1] >= rank[p2]:
                parents[p2] = p1
                rank[parents[p2]] += 1
            
            else:
                parents[p1] = p2
                rank[parents[p1]] += 1
            
            return True
        
        for node1, node2, in edges:
            if not union(node1, node2):
                return False
            count -= 1
        
        return count == 1

        