# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return 
        def find_vals(root,lev,val_lev):
            if not root: return
            if lev not in val_lev.keys():
                val_lev[lev]=[root.val]
            else: val_lev[lev]+=[root.val]
            find_vals(root.left,lev+1,val_lev)
            find_vals(root.right,lev+1,val_lev)
            return val_lev
        ans=[]
        for i in range(len(find_vals(root,0,{}))):
            ans.append(max(find_vals(root,0,{})[i]))
        return ans