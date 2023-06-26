# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans,cur,l,l2=head,head,0,0
        while cur:
            cur=cur.next
            l+=1
        while l2<l-n-1:
            ans=ans.next
            l2+=1
        if n==l:
            return head.next
        ans.next=ans.next.next
        return head