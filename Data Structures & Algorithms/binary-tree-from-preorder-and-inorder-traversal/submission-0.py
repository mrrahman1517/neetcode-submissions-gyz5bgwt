# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        rootVal = preorder[0]
        rindex = 0
        # find root in order list
        for i, node in enumerate(inorder):
            if node == rootVal:
                break
        # i is the position of root in inorder list
        inleft = inorder[:i]
        print (f"inleft: {inleft}")
        inright = inorder[i+1:]
        print (f"inright: {inright}")
        prleft = preorder[rindex + 1: rindex + 1 + len(inleft)]
        print (f"prleft: {prleft}")
        prright = preorder[rindex + 1 + len(inleft):]
        print (f"prright: {prright}")
        root = TreeNode(rootVal)
        if len(prleft) != 0:
            root.left = self.buildTree(prleft, inleft)
        if len(prright) != 0:
            root.right = self.buildTree(prright, inright)
        return root
        
        