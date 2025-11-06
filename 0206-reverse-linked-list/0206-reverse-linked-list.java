/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode recursion(ListNode prev, ListNode cur){
        if(cur == null){
            return prev; // 종료 조건
        }

        ListNode next = cur.next;
        cur.next = prev;
        prev = cur;
        return recursion(prev, next);
    }

    public ListNode reverseList(ListNode head) {
        return recursion(null, head);
    }
}
// 문제 정의: 단일 연결 리스트의 헤드가 주어졌을 때, 뒤집힌 리스트를 반환한다.
// 문제 해결: 각 노드를 순회하는데 이전 노드를 기억해서, 현재 노드가 이전 노드를 가리킨다.
// 단, 현재 노드에서는 이전 노드를 알 수 없기 떄문에 현재 노드를 보기 전에 미리 이전 노드를 기억해야 한다.

