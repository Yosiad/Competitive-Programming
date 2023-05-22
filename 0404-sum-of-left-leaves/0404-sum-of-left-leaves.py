# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack=[[root,0]]
        sum=0
        while stack:
            node,dire=stack.pop()
            if node.left: 
                stack.append([node.left,-1])
            if node.right:stack.append([node.right,1])
            if not node.left and not node.right and dire==-1: sum+=node.val
        return sum