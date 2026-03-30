# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoding = []
        def dfs(node):
            if not node:
                encoding.append("N")
                return
            encoding.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        result = ",".join(encoding) 
        print(result)
        return result

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(","))
        def dfs():
            val = next(vals)
            if val == "N":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root
