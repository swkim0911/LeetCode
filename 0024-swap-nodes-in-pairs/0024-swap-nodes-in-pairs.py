# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode(-1)
        root.next = head

        if head and head.next:
            b = head.next
            head.next = self.swapPairs(b.next)
            b.next = head

            prev.next = b

        return root.next
        