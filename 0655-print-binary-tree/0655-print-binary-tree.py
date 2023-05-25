# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        stack1=[[root,1]]
        root1=root
        prev_lev=1
        while stack1:
            node, lev=stack1.pop()
            if lev>prev_lev: prev_lev=lev
            if node.right: stack1.append([node.right,lev+1])
            if node.left: stack1.append([node.left,lev+1])
        ans=[]
        for i in range(prev_lev):
            tmp=[]
            for j in range(2**prev_lev-1):
                tmp.append("")
            ans.append(tmp)
        stack2=[[root1,0, 2**prev_lev-1,0]]
        while stack2:
            node,st,end,lev=stack2.pop()
            ans[lev][(st+end)//2]=str(node.val)
            if node.right: stack2.append([node.right,(st+end)//2+1,end,lev+1])
            if node.left: stack2.append([node.left,st,(st+end)//2,lev+1])
            
        return ans