class Solution:
    def sumBase(self, n: int, k: int) -> int:
        s=''
        ans=0
        if n//k==0:
            ans=n
        while n//k:
            s+=str(n%k)
            n=n//k
            if n//k==0:
                s+=str(n)
        for i in s:
            ans+=int(i)
        return ans