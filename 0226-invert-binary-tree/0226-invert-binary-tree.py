# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # 현재 node에서 invert한 상태를 반환한다.
    def invertTree(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return node
        
        left = self.invertTree(node.left)
        right = self.invertTree(node.right)
        
        node.left, node.right = right, left 
        return node
         
# 문제 정의: 주어진 이진 트리르 좌우 반전해서 root node를 반환합니다.
# 해결: 재귀를 사용해서 해결합니다. 
# invertTree 함수를 "현재 node에서 invert한 상태를 반환하는 함수"로 정의 했을 때,
# 왼쪽 서브트리에 대해 invertTree 함수를 호출해서 반환받은 결과값(inverted left sub-tree)과
# 오른쪽 서브트리에 대해 invertTree 함수를 호출해서 반환받은 결과값(inverted right sub-tree)을 
# 현재 노드 기준으로 왼쪽 서브 트리를 그 반환된 오른쪽 서브 트리에 대한 값, 그리고 현재 노드 기준으로 오른쪽 서브 트리를 
# 반환된 왼쪽 서브 트리에 대한 값을 서로 swapping 한다면
# 문제에서 요구하는 결과값을 받을 수 있습니다.




        

        