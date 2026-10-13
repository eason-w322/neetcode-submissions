# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = 0
        if not root:
            return 0
        maximum = root.val
        def dfs(node, maximum):
            nonlocal output
            if not node:
                return 
            if node.val >= maximum:
                output += 1
                maximum = node.val
            dfs(node.left, maximum)
            dfs(node.right, maximum)
        
        dfs(root, maximum)
        return output

            