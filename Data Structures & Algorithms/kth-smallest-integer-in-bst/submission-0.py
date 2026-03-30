# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # algorithm
        # if k < size of left subtree, then search in left subtree
        # if k > size of left subtree + 1, search in right subtree
        # else return root ????
        # we can probably avoid size computing by utilizing BST property
        # brute force do in order traversal and return kth element from the sorted list

        # idea, keep going down left
        # if k = 1, return the leftmost leaf
        # otherwise move up by one (backtrack) and check if right subtree exists
        # if it does to right and keep traversing left again
        self.k = k
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            inorder(node.right)
        inorder(root)
        return self.result
        

        