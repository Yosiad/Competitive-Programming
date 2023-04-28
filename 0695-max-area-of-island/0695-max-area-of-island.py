class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        h=len(grid); w=len(grid[0]); area=0; 
        def dfs(g, r, c):
            if 0<=r<h and 0<=c<w and g[r][c] == 1:
                g[r][c] = 0
                return 1 + dfs(g, r-1, c) + dfs(g, r, c+1) + dfs(g, r+1, c) + dfs(g, r, c-1)
            else: return 0
            
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 1:  area = max(area, dfs(grid, r, c))
                
        return area    