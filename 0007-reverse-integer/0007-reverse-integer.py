class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            x=int(str(x)[::-1])
            if x>2**31-1:
                x=0
        else:
            x=str(x)
            x=int(x[::-1][:-1])*-1
            if x<-2**31:
                x=0
        return x