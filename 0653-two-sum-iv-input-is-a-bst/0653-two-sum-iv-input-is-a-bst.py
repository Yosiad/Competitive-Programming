# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack=[root]
        values=[]
        while stack:
            node=stack.pop()
            for i in values: 
                if i+node.val==k:
                    return True
            values.append(node.val)
            if node.right:stack.append(node.right)
            if node.left: stack.append(node.left)
        return False