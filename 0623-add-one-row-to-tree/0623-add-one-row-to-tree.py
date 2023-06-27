# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if not root: return
        q=collections.deque([[root,1]])
        if depth==1:
            root1=TreeNode(val)
            root1.left=root
            return root1
        while q :
            node, dep=q.popleft()
            if dep==depth-1:
                tmp1=node.right
                tmp2=node.left
                if node.right or node.left:
                    node.right=TreeNode(val)
                    node.right.right=tmp1
                    node.left=TreeNode(val)
                    node.left.left=tmp2
                if not(node.right or node.left):
                    node.right=TreeNode(val)
                    node.left=TreeNode(val)
                    
            if node.right:q.append([node.right,dep+1])
            if node.left:q.append([node.left,dep+1])
            if dep>depth: break
        return root
            
            