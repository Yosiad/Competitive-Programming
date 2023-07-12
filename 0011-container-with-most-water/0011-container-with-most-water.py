class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum=0
        a=0
        b=len(height)-1
        while a<b:
            area=(b-a)*min(height[a],height[b])
            maximum=max(area, maximum)
            if height[a]<height[b]:
                a+=1
            else:
                b-=1
        return maximum