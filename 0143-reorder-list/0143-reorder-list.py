# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        queue=deque()
        cur=head
        while cur.next:
            queue.append(cur.next)
            cur= cur.next
        while queue:
            if head:
                tmp=queue.pop()
                head.next=tmp
                head=head.next
                if queue:
                    tmp=queue.popleft()
                    head.next=tmp
                    head=head.next
        head.next=None