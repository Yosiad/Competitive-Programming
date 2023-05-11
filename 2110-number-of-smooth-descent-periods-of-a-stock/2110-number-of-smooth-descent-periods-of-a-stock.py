class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        s=[1]*len(prices)
        for i in range(1,len(prices)):
            if prices[i]==prices[i-1]-1:
                s[i]=s[i-1]+1
        return sum(s)