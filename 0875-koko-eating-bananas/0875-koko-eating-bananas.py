class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        def can(speed):
            sum=0
            for i in piles:
                sum+=(i+speed-1)//speed
            return sum<=h
        while left<right:
            mid=(left+right)//2
            if can(mid):
                right=mid
            else:
                left=mid+1
        return left