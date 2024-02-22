class Solution:
    def climbStairs(self, n: int) -> int:
        a=0
        b=1
        c=1
        for i in range(n-1):
            a=b
            b=c
            c=a+b
        return c      