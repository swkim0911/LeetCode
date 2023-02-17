# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return head
        prev = head
        cursor = head.next
        count = 0

        while cursor and cursor.next:
            b = cursor.next
            prev.next = b
            cursor.next = b.next
            b.next = cursor

            if count:
                tmp = head
                for _ in range(count):
                    tmp = tmp.next

                e = tmp.next
                tmp.next = b
                b.next = e
                prev.next = cursor
                prev = prev.next

            else:
                prev = prev.next.next
            cursor = cursor.next

            count = count + 1

        return head
        