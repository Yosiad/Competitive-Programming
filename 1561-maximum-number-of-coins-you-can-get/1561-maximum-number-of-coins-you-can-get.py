class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sum=0
        a=1
        piles=sorted(piles)[::-1]
        for i in range(int(len(piles)/3)):
            sum+=piles[a]
            a+=2
        return sum