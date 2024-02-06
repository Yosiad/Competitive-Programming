class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves=0
        while maxDoubles and target != 1:
            if target%2==0:
                maxDoubles-=1
                target//=2
            else: 
                target-=1
            moves+=1
        moves+=target-1
        return moves
                