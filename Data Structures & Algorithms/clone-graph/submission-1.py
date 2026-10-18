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
            return None
        head = node
        copy = {}
        def dfs(node, copy):
            copy[node] = Node(val = node.val, neighbors = [])
            for neighbor in node.neighbors:
                if neighbor in copy:
                    continue
                dfs(neighbor, copy)
            
        
        dfs(node, copy)
        for node in copy:
            for neighbor in node.neighbors:
                copy[node].neighbors.append(copy[neighbor])
        
        return copy[head]
