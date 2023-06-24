class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r=0
        output=0
        for i in range(1,len(s)):
            if s[i]==s[0]:
                l=i
            if s[i]!=s[0]:
                r=i
                break
        output=max(output,r-l+1)
        a=r+1
        for j in range(a,len(s)):
            if s[j] not in s[l:j]:
                output=max(output,j-l+1)
            else:
                b=j-1
                while b>=l:
                    if s[b]==s[j]:
                        l=b+1
                        break
                    b-=1
                output=max(output,j-l+1)
        if len(s)==0:
            output=0
        return output