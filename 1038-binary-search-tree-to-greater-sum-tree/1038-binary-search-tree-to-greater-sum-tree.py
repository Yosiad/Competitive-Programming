# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def find_vals(root):
            if not root: return []
            return find_vals(root.left)+[root.val]+find_vals(root.right)
        vals=find_vals(root)
        def buildTree(root):
            if not root: return 
            sum=0
            for i in vals:
                if i>root.val: sum+=i
            root.val+=sum
            buildTree(root.left)
            buildTree(root.right)
            return root
        return buildTree(root)
         
            