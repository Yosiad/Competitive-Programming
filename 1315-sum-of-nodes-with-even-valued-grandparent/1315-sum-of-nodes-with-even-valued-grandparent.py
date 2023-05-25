# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        val_lev=collections.defaultdict(list)
        stack=[[root,0]]
        ans=0
        while stack:
            node,lev=stack.pop()
            if lev-2 in val_lev.keys() and val_lev[lev-2]%2==0: ans+=node.val
            val_lev[lev]=node.val
            if node.right: stack.append([node.right,lev+1])
            if node.left: stack.append([node.left,lev+1])
        return ans
        