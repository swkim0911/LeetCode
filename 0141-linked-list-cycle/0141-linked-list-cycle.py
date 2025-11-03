# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

# 문제 정의: 링크드 리스트에 순환이 있는지 찾아야 한다. 단, 메모리 공간은 상수(O(1))이어야 한다.
# 해결: 순환이 없다는 건 언젠가는 None인 노드를 만나는 것이니까 head 부터 쭉 순회해서 None을 찾으면 되지만 이때 메모리 공간을 O(n)을 차지하므로 부적절하다.
# 해결방법은 링크드 리스트의 헤드를 가리키는 두 개의 포인터를 두고, 하나는 1칸씩, 다른 하나는 2칸씩 앞으로 보내서 두 포인터가 같은 노드를 가리키는 순간이 있으면 해당 링크드 리스트는 순환이 있는 것이고, 어느 순간 None을 만나면 순환이 없는 것이다.
# 이 방법은 모든 노드를 순회하며 확인하지 않고 포인터가 두 칸씩 확인하니까 O(n) 메모리 공간이 필요없이 O(1)이면 된다.