# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.mpath = float('-inf')
        def maxPathSumHelper(node):
            if not node:
                return 0
            leftMax = max(0, maxPathSumHelper(node.left))
            rightMax = max(0, maxPathSumHelper(node.right))
            self.mpath = max(self.mpath, leftMax + rightMax + node.val)
            return node.val + max(leftMax, rightMax)
        maxPathSumHelper(root)
        return self.mpath
