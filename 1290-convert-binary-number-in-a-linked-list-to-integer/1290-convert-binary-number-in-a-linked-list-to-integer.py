# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head: return 
        if not head.next: return head.val
        num=head.val
        while head.next:
            num*=2
            if head.next.val==1: num+=1
            head=head.next
        return num
            
            
            