# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        cursor1 = head
        cursor2 = head

        while cursor1.next:
            cursor1 = cursor1.next

        while cursor2.next.next:
            cursor2 = cursor2.next

        cursor2.next = None

        cursor1.next = self.reverseList(head)

        return cursor1