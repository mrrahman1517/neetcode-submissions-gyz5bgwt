# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        rootVal = preorder[0]
        # find root in order list
        # i is the position of root in inorder list
        i = inorder.index(rootVal)
        inleft = inorder[:i]
        inright = inorder[i+1:]
        prleft = preorder[1: 1 + i]
        prright = preorder[1 + i:]
        root = TreeNode(rootVal)
        if len(prleft) != 0:
            root.left = self.buildTree(prleft, inleft)
        if len(prright) != 0:
            root.right = self.buildTree(prright, inright)
        return root