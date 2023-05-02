# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def find_vals(root):
            if not root: return []
            return find_vals(root.left)+[root.val]+find_vals(root.right)
        arr=find_vals(root)
        def build_tree(root,arr):
            if not root: return 
            sum=0
            for i in arr: 
                if i>=root.val: sum+=i
            root.val=sum
                    
            build_tree(root.left,arr)
            build_tree(root.right,arr)
            return root
        return build_tree(root,arr)
    