class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        elif n==1:
            return 10
        else:
            a=9
            b=9
            c=n-1
            while c:
                b*=a
                a-=1
                c-=1
            return b+self.countNumbersWithUniqueDigits(n-1)