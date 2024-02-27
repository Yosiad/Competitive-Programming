class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s))!=len(set(t)):
            return False
        d={}
        for i in range(len(s)):
            if s[i] in d and d[s[i]]!=t[i]:
                return False
            d[s[i]]=t[i]
        return True