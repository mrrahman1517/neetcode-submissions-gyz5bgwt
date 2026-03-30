# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        lk = k
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            lk -= 1
            if lk == 0:
                return curr.val
            curr = curr.right