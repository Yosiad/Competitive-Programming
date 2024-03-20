# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.arr=[]
        def getString(root,conc):
            if not root:
                return
            conc+=chr(root.val+97)
            if not root.right and not root.left:
                self.arr.append(conc[::-1])
            getString(root.left,conc)
            getString(root.right,conc)
            return sorted(self.arr)[0]
        return getString(root,'')