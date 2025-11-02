# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. 루트 노드에서 시작해서 p,q 노드까지 어떤 노드를 거치는지 기록. (node -> p, node -> q)
        # 이때 p,q 노드를 찾아가는 과정이 BST이기 때문에 탐색이 쉽다.

        if not root:
            return root
        
        cur = root
        p_route = [cur]

        while cur.val != p.val:
            if cur.val < p.val:
                cur = cur.right
            else:
                cur = cur.left
            p_route.append(cur)

        cur = root
        q_route = [cur]

        while cur.val != q.val:
            if cur.val < q.val:
                cur = cur.right
            else:
                cur = cur.left
            q_route.append(cur)

        # 2. 그 기록을 봐서 가장 나중에 겹치는 노드가 LCA이다.
        min_len = min(len(p_route), len(q_route))
        answer = None
        for i in range(min_len - 1, -1, -1):

            if p_route[i].val == q_route[i].val:
                answer = p_route[i]
                break
        return answer



# 이진 탐색 트리에서 최소 공통 조상 찾기
# 이진 탐색 트리 특징: 부모 노드에서 양쪽 노드를 봤을 때, 왼쪽 노드는 부모 노드보다 값이 작고, 오른쪽 노드는 부모 노드보다 값이 크다. 모든 노드의 값은 unique하다.

        