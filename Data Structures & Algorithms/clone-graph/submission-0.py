"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        seen = {}
        start = node
        seen[start] = Node(val = node.val)
        visited = deque()
        visited.append(node)

        while visited:
            root = visited.popleft()
            for node in root.neighbors:
                if node in seen:
                    continue
                visited.append(node)
                seen[node] = Node(val = node.val)
    
        for node in seen:
            seen[node].neighbors = [seen[i] for i in node.neighbors]
    
        return seen[start]

        