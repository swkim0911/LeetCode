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
import java.util.*;

class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null) return head;
        Stack<Integer> stack = new Stack<>();
        ListNode cur = head;
        stack.push(cur.val);
        while(cur.next != null && cur.next != head){ // recursion을 고려했을 떄.
            cur = cur.next;
            stack.push(cur.val);
        }
        ListNode reversedListHead = new ListNode(stack.pop());
        ListNode reversedListcur = reversedListHead;
        while(!stack.isEmpty()){
            reversedListcur.next = new ListNode(stack.pop());
            reversedListcur = reversedListcur.next;
        }
        return reversedListHead;
    }
}
// 문제 정의: 싱글 링크드 리스트의 헤드가 주어졌을 떄, 뒤집힌 리스트를 반환한다.
// 해결: 