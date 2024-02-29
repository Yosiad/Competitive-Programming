class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr=s.split(' ')
        s={}
        if len(set(arr))!=len(set(pattern)):
            return False
        if len(arr)!=len(pattern):
            return False
        for i in range(len(arr)):
            if pattern[i] in s and s[pattern[i]]!=arr[i]:
                return False
            s[pattern[i]]=arr[i]
        return True