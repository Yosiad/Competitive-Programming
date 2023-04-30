# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        def find_val(root):
            if not root: return []
            return find_val(root.left)+[root.val]+find_val(root.right)
        arr_val=sorted(find_val(root)+[val])
        def build_tree(arr):
            if not arr: return
            root=TreeNode(arr[len(arr)//2])
            root.left=build_tree(arr[:len(arr)//2])
            root.right=build_tree(arr[len(arr)//2+1:])
            return root
        return build_tree(arr_val)
        