class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        count = 0
        
        def union(x1, x2):
            nonlocal count
            p1 = find(x1)
            p2 = find(x2)
            if p1 != p2:
                count += 1

                if size[p1] >= size[p2]:
                        parents[p2] = p1
                        size[p1] += size[p2]
                else:
                    parents[p1] = p2
                    size[p2] += size[p1]
        
        for x1, x2 in edges:
            union(x1, x2)
        return n - count
                
            