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

# 문제 정의: 트리의 모든 노드에서 왼쪽, 오른쪽 서브트리의 높이 차이가 1 이하이면 True, 아니면 False를 반환해야 한다.
# 풀이: 각 노드들을 방문해서 왼쪽, 오른쪽 서브트리를 높이를 찾기 위해서 재귀를 이용한다.
# get_height 함수는 재귀로 각 노드의 높이를 구한다. (leaf 노드의 height = 0)
# 어떤 노드에서 양쪽 서브트리의 높이를 모두 구하고 비교했을 떄, 그 높이 차이가 2 이상이면 전역 인스턴스 변수로 선언한 is_balanced 변수를 False로 처리한다.