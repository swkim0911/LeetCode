# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = cursor = ListNode(-1)
        tmp_list = []

        for node in lists:
            while node:
                tmp_list.append(node.val)
                node = node.next

        tmp_list.sort()

        for node in tmp_list:
            cursor.next = ListNode(node)
            cursor = cursor.next

        return head.next
        