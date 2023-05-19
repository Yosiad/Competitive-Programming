# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:return 0
        q=collections.deque([[root,[root.val],root.val]])
        ans=0
        while q: 
            node, nums,totsum=q.popleft() 
            cursum=totsum
            if totsum==targetSum: ans+=1
            for i in range(len(nums)-1):
                cursum-=nums[i]
                if cursum==targetSum: 
                    ans+=1
            if node.left: q.append([node.left,nums+[node.left.val],totsum+node.left.val])
            if node.right: q.append([node.right,nums+[node.right.val],totsum+node.right.val]) 
        return ans  
            