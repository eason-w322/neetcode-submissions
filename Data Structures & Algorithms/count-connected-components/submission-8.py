class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        
        def find(x):
            while x != parents[x]:
                x = find(parents[x])
            return x
        
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)
            if p1 == p2:
                return False
            if p1 != p2:
                parents[p1] = p2
            return True
        
        total_component = n
        for x1, x2 in edges:
            if union(x1, x2):
                total_component -= 1
        
        return total_component

            