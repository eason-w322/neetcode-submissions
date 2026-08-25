class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n + 1)]
        rank = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(a, b):
            p1 = find(a)
            p2 = find(b)
            if p1 == p2:
                return False
            if rank[p1] <= rank[p2]:
                parents[p1] = p2
            else:
                parents[p2] = p1
            return True
        
        count = n
        for node1, node2 in edges:
            if union(node1, node2):
                count -= 1
        
        return count