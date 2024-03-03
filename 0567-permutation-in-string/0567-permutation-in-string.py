class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        for r in range(len(s1)-1,len(s2)):
            if sorted(s1)==sorted(s2[l:r+1]):
                return True
                break
            l+=1
        return False 