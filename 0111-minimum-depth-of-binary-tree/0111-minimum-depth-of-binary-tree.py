# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        ans=0
        if not root:
            return 0
        while root and (not root.right or not root.left) and (root.right or root.left):
            if not root.right:
                root=root.left
                ans+=1
            if not root.left:
                root=root.right
                ans+=1
        def help(root):
            if not root:
                return 0
            return min(self.minDepth(root.left),self.minDepth(root.right))+1
        return ans+help(root)  