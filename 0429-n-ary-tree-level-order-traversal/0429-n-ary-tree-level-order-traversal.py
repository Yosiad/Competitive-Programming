"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return
        ans=collections.defaultdict(list)
        q=collections.deque([[root,0]])
        while q:
            node,lev=q.popleft()
            ans[lev].append(node.val)
            if node.children:
                for nodes in node.children:
                    q.append([nodes,lev+1])
        return list(ans.values())
         