"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return
        stack=[root]
        ans=[]
        while stack:
            node=stack.pop()
            ans.append(node.val)
            lev=[]
            if node.children:
                for nodes in node.children:
                    lev.append(nodes)
            stack+=lev[::-1]
        return ans