# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        results = []
        def dfs(node):
            if not node:
                results.append("None")
                return
            results.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(results)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        data = deque(data)
        def dfs(data):
            if not data or data[0] == "None":
                data.popleft()
                return
            root = TreeNode(val = int(data.popleft()))
            root.left = dfs(data)
            root.right = dfs(data)
            return root
        return dfs(data)
        

        
