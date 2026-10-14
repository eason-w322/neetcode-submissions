# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maximum = -float("inf")
        def dfs(node):
            nonlocal maximum
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            maximum = max(maximum, left_sum + right_sum + node.val, node.val, node.val + max(left_sum, right_sum))
            return max(max(left_sum, right_sum) + node.val, node.val)
        dfs(root)
        return maximum
