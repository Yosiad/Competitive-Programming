# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        q=deque([[root,1,0]])
        prev_num,prev_lev=1,0
        while q:
            node,num,level=q.popleft()
            if level>prev_lev:
                prev_lev=level
                prev_num=num
            ans=max(ans,num-prev_num+1)
            if node.left:
                q.append([node.left,num*2,level+1])
            if node.right:
                q.append([node.right,num*2+1,level+1])
        return ans