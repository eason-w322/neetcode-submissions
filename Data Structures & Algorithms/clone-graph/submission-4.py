"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        head = node
        clone = {}
        visited = set()
        def dfs(node):
            if node in visited:
                return 
            clone[node] = Node(val = node.val)
            visited.add(node)
            for neighbor in node.neighbors:
                dfs(neighbor)
        
        dfs(node)
        
        for node in clone:
            for neighbor in node.neighbors:
                clone[node].neighbors.append(clone[neighbor])
        
        return clone[head]
        

            

        
