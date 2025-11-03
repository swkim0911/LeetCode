# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.is_balanced = True  # 인스턴스 변수로 선언

    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return -1
        
        left_depth = self.get_height(node.left)
        right_depth = self.get_height(node.right)

        if abs(left_depth - right_depth) > 1:
            self.is_balanced = False

        return 1 + max(left_depth, right_depth)


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.get_height(root)
        return self.is_balanced