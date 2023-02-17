# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        odd = head
        even_head = even = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head

        return head
    
# 나는 2,3번째 4,5번째 노드를 방문하면서 서로 위치를 바꾸고
# 또 후 처리로 n/2 번 for문을 돌아서 추가 연산이 필요했다.
# 따라서 시간 복잡도가 너무 컸음. > n^2

# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None:
#             return head
#
#         prev = head
#         cursor = head.next
#         count = 0
#
#         while cursor and cursor.next:
#             b = cursor.next
#             prev.next = b
#             cursor.next = b.next
#             b.next = cursor
#
#             if count:
#                 tmp = head
#                 for _ in range(count):
#                     tmp = tmp.next
#
#                 e = tmp.next
#                 tmp.next = b
#                 b.next = e
#                 prev.next = cursor
#                 prev = prev.next
#
#             else:
#                 prev = prev.next.next
#             cursor = cursor.next
#
#             count = count + 1
#
#         return head
        
