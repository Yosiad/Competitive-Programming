# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find(root):
            if not root: return []
            return [root.val]+find(root.left)+find(root.right)
        return sorted(find(root))[k-1]