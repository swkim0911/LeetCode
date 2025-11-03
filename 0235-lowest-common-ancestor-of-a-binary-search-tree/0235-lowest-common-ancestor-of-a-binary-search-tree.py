# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                break

        return cur

# 문제 정의: bst에서 두 노드의 최소 공통 부모 노드 찾기
# 풀이: 문제에서 bst 조건을 줬기 때문에 bst 특징을 활용해야 한다. bst에서 부모 노드와 자식 노드를 비교했을 떄, 왼쪽 자식 노드는 부모 노드보다 작고, 오른쪽 자식 노드는 부모 노드보다 크다.
# 그리고 값들은 unique한 특징이 있다.
# BST에서 최소 공통 조상을 찾기 위해서 정렬의 특징을 사용할 수 있다. root 노드(부모 노드)에서 찾는 노드 p, q가 모두 왼쪽에 있다면 root는 아직 LCA가 아니며 LCA를 찾기 위해 왼쪽 서브트리의 root 노드를 다시 탐색한다.
# 반대 오른쪽 서브트리에서 같은 논리이다.
# 단, 만약에 부모 노드에서 왼쪽 노드와 오른쪽 노드 각각에 p,q가 있다면 그 부모 노드가 LCA가 된다.