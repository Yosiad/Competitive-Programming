# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        val_len={}
        sum=0
        def create_dic(root, ind):
            if not root: return
            if not root.right and not root.left:
                if ind not in val_len.keys():
                    val_len[ind]=root.val
                else:val_len[ind]+=root.val
            create_dic(root.left, ind+1)
            create_dic(root.right, ind+1)
        create_dic(root, 0)
        return val_len[max(list(val_len.keys()))]