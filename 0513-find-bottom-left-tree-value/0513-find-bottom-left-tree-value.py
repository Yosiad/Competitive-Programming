# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return
        stack=[[root,0]]
        ans=[root.val,0]
        while stack:
            node, dep=stack.pop()
            if  ans[1] < dep:
                ans=[node.val, dep]
            if node.right: stack.append([node.right, dep+1])
            if node.left: stack.append([node.left, dep+1])    
        return ans[0]