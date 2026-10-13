# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        results = []
        visited = deque()
        visited.append(root)

        while visited:
            level = []
            for _ in range(len(visited)):
                node = visited.popleft()
                level.append(node.val)
                
                if node.left:
                    visited.append(node.left)
                if node.right:
                    visited.append(node.right)
            results.append(level)
        return results


