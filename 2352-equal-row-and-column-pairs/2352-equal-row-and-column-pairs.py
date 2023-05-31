class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans=0
        s={}
        for k in grid:
            if tuple(k) in s.keys():
                s[tuple(k)]+=1
            else: 
                s[tuple(k)]=1
        for i in range(len(grid[0])):
            b=[]
            for j in grid:
                b.append(j[i])
            if tuple(b) in s.keys(): ans+=s[tuple(b)]
        return ans
