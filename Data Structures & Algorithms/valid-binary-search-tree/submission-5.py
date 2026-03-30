# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        pos_inf = float('inf')
        neg_inf = float('-inf')
        def isValidRange(left, right, node):
            if not (left < node.val < right):
                return False
            lflag = True
            rflag = True
            if node.left:
                lflag = isValidRange(left, node.val, node.left) 
            if node.right:
                rflag =  isValidRange(node.val, right, node.right)
            return lflag and rflag
        return isValidRange(neg_inf, pos_inf, root)
        