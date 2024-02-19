class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=''
        if s==s[::-1]:
            return s
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                if s[i:j]==s[i:j][::-1]:
                    if ans=='':
                        ans=s[i:j]
                    else:
                        if len(s[i:j])>len(ans):
                            ans=s[i:j]
        return ans