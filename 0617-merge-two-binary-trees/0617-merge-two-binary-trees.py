# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def build(root1,root2):
            if not root1 and not root2:
                return None
            if root1 and not root2: return root1
            elif not root1 and root2: return root2
            else: root=TreeNode(root1.val+root2.val)    
            root.left=build(root1.left,root2.left)  
            root.right=build(root1.right,root2.right)
            return root   
        return build(root1,root2)