# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:return
        q=collections.deque([[root,[root.val],root.val]])
        ans=[]
        while q: 
            node, nums,totsum=q.popleft()  
            if node.left: q.append([node.left,nums+[node.left.val],totsum+node.left.val])
            if node.right: q.append([node.right,nums+[node.right.val],totsum+node.right.val]) 
            if not node.right and not node.left and totsum==targetSum:
                ans.append(nums)
        return ans   