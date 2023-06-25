"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        q=collections.deque([[root,0]])
        prev=0
        while q:
            node, lev=q.popleft()
            if not q or lev<q[0][1]:
                node.next=None
            else: node.next=q[0][0]
            if node.left: q.append([node.left,lev+1])
            if node.right: q.append([node.right,lev+1])
        return root