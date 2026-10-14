# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val : idx for idx, val in enumerate(inorder)}
        pre_index = 0

        def dfs(left, right):
            nonlocal pre_index
            if left > right:
                return
            root = TreeNode(val = preorder[pre_index])
            mid = pos[preorder[pre_index]]
            pre_index += 1
            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)
            return root

        return dfs(0, len(preorder) - 1)