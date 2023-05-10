# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return
        def traverse_zig(root,lev,val_lev):
            if not root: return
            if lev not in val_lev.keys(): val_lev[lev]=[root.val]
            else:
                if lev%2==0: val_lev[lev].append(root.val)
                else: val_lev[lev].insert(0,root.val)
            traverse_zig(root.left,lev+1,val_lev)
            traverse_zig(root.right,lev+1,val_lev)
            return val_lev.values()
        ans=[]
        for i in traverse_zig(root,0,{}): ans.append(i)
        return ans