# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        if not head:
            return 
        cur=head
        while cur and cur.next:
            if cur.next.val==val:
                temp=cur.next
                while temp and temp.val==val:
                    temp=temp.next
                cur.next=temp
            cur=cur.next
        return head