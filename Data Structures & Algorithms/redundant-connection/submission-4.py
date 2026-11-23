class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]

        def find(x):
            while x != parents[x]:
                x = parents[x]
            return x
        
        def union(x1, x2):
            p1 = find(x1)
            p2 = find(x2)
            if p1 == p2:
                return False
            else:
                parents[p1] = p2
                return True
        
        for x1, x2 in edges:
            if not union(x1, x2):
                return [x1, x2]


