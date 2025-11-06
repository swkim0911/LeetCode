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
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;

        while(head != null){
            ListNode nxt = head.next;
            head.next = prev;

            prev = head;
            head = nxt;
        }

        return prev;



    }
}
// 문제 정의: 단일 연결 리스트의 헤드가 주어졌을 때, 뒤집힌 리스트를 반환한다.
// 문제 해결: 각 노드를 순회하면서 이전 노드를 기억해서, 현재 노드가 이전 노드를 가리킨다.