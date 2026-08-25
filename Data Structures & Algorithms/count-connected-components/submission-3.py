class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(0, n + 1)]
        rank = [0] * (n + 1)
        count = n

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(node1, node2):
            nonlocal count
            p1 = find(node1)
            p2 = find(node2)
            if p1 != p2:
                count -= 1
                if rank[p1] > rank[p2]:
                    parents[p2] = p1
                elif rank[p1] < rank[p2]:
                    parents[p1] = p2
                else:
                    parents[p1] = p2
                    rank[p2] += 1
            
        for node1, node2 in edges:
            union(node1, node2)
        return count