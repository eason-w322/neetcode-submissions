# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        results = []
        def dfs(node):
            nonlocal results
            if not node:
                return
            dfs(node.left)
            results.append(node.val)
            dfs(node.right)
        dfs(root)
        temp = results[0]
        for i in range(1, len(results)):
            if temp >= results[i]:
                return False
            temp = results[i]
        return True