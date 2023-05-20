class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        stack=[[graph[0],[0]]]
        while stack:
               children,path=stack.pop()
               for child in children:
                    if child==len(graph)-1: ans.append(path+[child])
                    else: stack.append([graph[child],path+[child]])
                
        return ans