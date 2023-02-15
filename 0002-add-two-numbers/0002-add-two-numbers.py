# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_list = []
        carry = 0
        while l1 and l2:
            sum = 0
            if carry == 1:
                sum = 1 + l1.val + l2.val
                carry = 0
            else:
                sum = l1.val + l2.val

            if sum >= 10:
                result_list.append(sum - 10)
                carry = 1
            else:
                result_list.append(sum)

            while l1.next is None and l2.next is not None:
                l2 = l2.next
                sum = l2.val + 0 + carry
                if sum >= 10:
                    result_list.append(sum - 10)
                    carry = 1
                else:
                    result_list.append(sum)
                    carry = 0

            while l2.next is None and l1.next is not None:
                    l1 = l1.next
                    sum = l1.val + 0 + carry
                    if sum >= 10:
                        result_list.append(sum - 10)
                        carry = 1
                    else:
                        result_list.append(sum)
                        carry = 0

            l1 = l1.next
            l2 = l2.next

        if carry == 1:
            result_list.append(1)
    
        result = ListNode(-1)
        cursor = result
        for num in result_list:
            cursor.next = ListNode(num)
            cursor = cursor.next
        
        return result.next
        
        
        