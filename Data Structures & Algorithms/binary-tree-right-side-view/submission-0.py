# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side_view = []
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
            right_side_view.append(level[-1])
        return right_side_view



        