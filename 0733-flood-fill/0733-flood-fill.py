class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        col=image[sr][sc]
        seen=set()
        def modify(s,e):
            if(s<0 or e<0 or s>len(image)-1 or e>len(image[0])-1 or (s,e) in seen or image[s][e]!=col):
                return
            image[s][e]=color 
            seen.add((s,e))
            modify(s+1,e)
            modify(s-1,e)
            modify(s,e+1)
            modify(s,e-1)
            return image
        return modify(sr,sc) 