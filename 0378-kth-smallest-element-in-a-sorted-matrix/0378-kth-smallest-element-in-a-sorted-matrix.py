class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ans=[]
        for i in matrix:
            ans+=i
        return sorted(ans)[k-1] 