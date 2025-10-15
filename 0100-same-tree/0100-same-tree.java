/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null && q == null) return true;
        if(p == null || q == null) return false;
        if(p.val != q.val) return false;

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
}

/**
이 문제의 요구사항은 두 이진 트리가 같은지 같지않은지 확인하는 함수를 구현하느 것인데. 두 트리가 같다는 것은 같은 형태를 갖고, 그 형태의 각각의 노드의 값이 같을 때. 두 트리가 같다고 할 수 있습니다.

그래서 두 트리에 대해서 노드들을 방문하면서 같은지 확인할 수 있는데. 이때 bfs나 dfs 알고리즘을 사용할 수 있습니다. 두 경우 가능하지만 두 트리 모두 노드 개수가 100개 미만이기 때문에 dfs를 사용해도 메모리 공간 사용은 충분하다 생각이 들어 dfs를 사용하겠습니다.

isSameTree 함수를 dfs 재귀 함수라고 생각했을 때 종료 조건에 대해 생각해보겠습니다. 매개변수로 두 트리에 대한 현재 노드가 있는데. 각 노드의 값이 다르다면 다른 트리이기 때문에 false를 반환하게 종료할 수 있습니다.

그리고 example 2와 같이 한 쪽 트리에는 노드가 있고, 다른 쪽의 null 인 경우에도 두 트리가 달라서. 이를 종료조건으로 두겠습니다.
example 3처럼 모든 노드를 방문해서 모양과 그 값이 같을 때 isSameTree 함수는 매개변수 모두 null이므로 이 경우는 같다고 봅니다. (혹은 두 트리의 노드 개수가 1일 때, 양쪽 자식 모두 null입니다.)

이렇게 종료조건을 모두 구현하고 재귀 부분을 구현한다면 왼쪽 자식에 대해 재귀적으로 확인하고, 오른쪽 자식에 대해 재귀적으로 확인했을 떄, 모두 같다고(true)를 반환한다면 전체 트리는 같다고 볼 수 있습니다.

 */