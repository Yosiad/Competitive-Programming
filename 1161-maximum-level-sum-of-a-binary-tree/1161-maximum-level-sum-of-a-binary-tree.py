# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        val_lev={}
        def find_sum(root,lev):
            if not root: return
            if lev not in val_lev.keys():
                val_lev[lev]=root.val
            else: val_lev[lev]+=root.val
            find_sum(root.left,lev+1)
            find_sum(root.right,lev+1)
        find_sum(root,0)
        return list(val_lev.values()).index(max(val_lev.values()))+1
            