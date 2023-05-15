class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(grid,row,col,seen):
            if row<0 or row>=len(grid) or col<0 or col>=len(grid[0]) or grid[row][col]==0 or (row,col) in seen: return 0
            seen.append((row,col))
            return dfs(grid,row+1,col,seen) + dfs(grid,row-1,col,seen)+dfs(grid,row,col+1,seen)+dfs(grid,row,col-1,seen)+grid[row][col]
        ans=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]!=0:
                    ans=max(ans,dfs(grid,row,col,[]))
        return ans  