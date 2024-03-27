# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p,q):
            if p==None and q==None: return True
            if (q==None and p) or (p==None and q) or p.val != q.val: return False
            return check(p.right, q.right) and check(p.left, q.left)
        return check(p,q)