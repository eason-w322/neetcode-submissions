class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(0, n)]
        rank = [0] * n
        def find(x):
            if x != parents[x]:
                x = find(parents[x])
            return x
        
        count = n
        def union(x1, x2):
            nonlocal count
            p1 = find(x1)
            p2 = find(x2)
            if p1 != p2:
                count -= 1
                if rank[p1] > rank[p2]:
                    parents[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parents[p1] = p2
                    rank[p2] += rank[p1]
        
        for x, y in edges:
            union(x, y)
        return count

            