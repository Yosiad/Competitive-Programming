# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return
        mov=head
        l=0
        while mov.next:
            if not l%2: mov.val, mov.next.val=mov.next.val, mov.val
            mov=mov.next
            l+=1
        return head
            
        