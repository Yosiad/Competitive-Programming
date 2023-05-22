# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return
        q=collections.deque([[root,0]])
        ans=[]
        prevnum,prevlev=root.val,0
        while q:
            node, lev=q.popleft()
            if prevlev!=lev: 
                ans.append(prevnum)
                prevlev=lev
                prevnum=node.val
            else: prevnum=node.val
            if node.left: q.append([node.left,lev+1])
            if node.right: q.append([node.right,lev+1])
        ans.append(prevnum)
        return ans