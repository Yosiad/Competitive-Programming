# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n==1:
            return 1
        def checkBad(a,n):
            if isBadVersion(n) and not isBadVersion(n-1):
                return n
            c=(a+n)//2
            if isBadVersion(c) and not isBadVersion(c-1):
                return c
            if isBadVersion(c) and isBadVersion(c-1):
                return checkBad(a,c)
            else: return checkBad(c,n)
        return checkBad(1,n)
