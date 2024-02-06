class Solution:
    def numSteps(self, s: str) -> int:
        s=s[::-1]
        num,power,steps=0,0,0
        for i in s:
            if i=='1':num+=2**power
            power+=1
        while num != 1:
            if num%2==0: num//=2
            else: num+=1
            steps+=1
        return steps