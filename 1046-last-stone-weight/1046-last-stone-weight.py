class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)>1:
            stones=sorted(stones)
            if stones[-1]==stones[-2]:
                stones.pop()
                stones.pop()
            else:
                stones.append(stones[-1]-stones[-2])
                stones.pop(-2) 
                stones.pop(-2)
        if stones:return stones[0]  
        return 0