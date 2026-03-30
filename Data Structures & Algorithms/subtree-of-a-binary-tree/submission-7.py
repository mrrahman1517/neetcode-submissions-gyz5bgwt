# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 

    def isSametree(self, first, second):
        if not first and not second:
            return True
        if not first or not second:
            return False
        if first.val != second.val:
            return False
        return self.isSametree(first.left, second.left) and self.isSametree(first.right, second.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # bruteforce traverse everynode of the first tree in dfs order, for each visited node
        # run isSameTree check, too expensive
        # try 
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSametree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        