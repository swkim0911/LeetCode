# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import sys

sys.setrecursionlimit(10**9)

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        left = self.invertTree(root.left)

        right = self.invertTree(root.right)
        

        root.left, root.right = right, left 
    
        return root
         


# left -> right -> parent
# parent로 왔을 때 left(subtree)와 right(subtree)


        

        