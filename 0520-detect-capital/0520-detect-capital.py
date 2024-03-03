class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        n=len(word)
        if n==1:
            return True
        if n==2:
            if ord(word[0])>=90 and ord(word[1])<90 : 
                    return False
            else:
                return True
        if n>=3:
            for i in range(n-1):
                if ord(word[i])>90 and ord(word[i+1])<=90 : 
                    return False
                    break
                if i==n-2:
                    if ord(word[i])<=90 and ord(word[i+1])>90 : 
                        return False
                        break
                if n>=4 and i<n-1 and i>=1:
                    if ord(word[i-1])<=90 and ord(word[i])<=90 and ord(word[i+1])>90:
                        return False
                        break
            return True