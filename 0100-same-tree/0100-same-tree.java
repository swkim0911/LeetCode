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
import java.util.*;

class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        Queue<TreeNode> pTree = new LinkedList<>();
        Queue<TreeNode> qTree = new LinkedList<>();
        pTree.add(p);
        qTree.add(q); // ✅ q를 추가해야 함

        while (!pTree.isEmpty() && !qTree.isEmpty()) {
            TreeNode pNode = pTree.poll();
            TreeNode qNode = qTree.poll();

            if (pNode == null && qNode == null) continue; // 둘 다 null이면 계속
            if (pNode == null || qNode == null) return false; // 한쪽만 null이면 다름
            if (pNode.val != qNode.val) return false;

            pTree.add(pNode.left);
            pTree.add(pNode.right);
            qTree.add(qNode.left);
            qTree.add(qNode.right);
        }

        return pTree.isEmpty() && qTree.isEmpty(); // 남은 게 없어야 동일
    }
}