class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            l=0
            for i in range(len(needle)-1,len(haystack)):
                if needle==haystack[l:i+1]:
                    return l
                    break
                l+=1